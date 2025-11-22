"""
Job search service with data normalization, deduplication, and persistence.

This service coordinates job searches across multiple sources, normalizes data,
handles duplicate detection, and manages job persistence to the database.
"""

from typing import List, Dict, Optional, Set, Tuple, Any
from datetime import datetime, timedelta, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_, or_
import logging
import hashlib
from collections import defaultdict

from src.models.database import Job, Company, SearchQuery, EmploymentType, RemotePolicy
from src.scrapers.jobspy_client import JobSpyClient, get_jobspy_client

logger = logging.getLogger(__name__)


class JobCache:
    """Simple in-memory cache for job search results."""

    def __init__(self, ttl_seconds: int = 300):
        """
        Initialize cache with TTL.

        Args:
            ttl_seconds: Time to live for cache entries (default 5 minutes)
        """
        self.ttl_seconds = ttl_seconds
        self._cache: Dict[str, Tuple[datetime, List[Job]]] = {}

    def get(self, key: str) -> Optional[List[Job]]:
        """Get cached results if not expired."""
        if key in self._cache:
            timestamp, results = self._cache[key]
            if datetime.now(timezone.utc) - timestamp < timedelta(seconds=self.ttl_seconds):
                logger.debug(f"Cache hit for key: {key}")
                return results
            else:
                del self._cache[key]
                logger.debug(f"Cache expired for key: {key}")
        return None

    def set(self, key: str, results: List[Job]) -> None:
        """Cache results with current timestamp."""
        self._cache[key] = (datetime.now(timezone.utc), results)
        logger.debug(f"Cached {len(results)} results for key: {key}")

    def clear(self) -> None:
        """Clear all cached results."""
        self._cache.clear()
        logger.debug("Cache cleared")


class JobSearchService:
    """
    Service for searching, normalizing, and managing job data.

    Handles job searches across multiple platforms, data normalization,
    duplicate detection, company management, and database persistence.
    """

    def __init__(
        self,
        jobspy_client: Optional[JobSpyClient] = None,
        cache_ttl: int = 300,
    ):
        """
        Initialize job search service.

        Args:
            jobspy_client: JobSpy client instance (creates default if None)
            cache_ttl: Cache time-to-live in seconds (default 5 minutes)
        """
        self.jobspy_client = jobspy_client or get_jobspy_client()
        self.cache = JobCache(ttl_seconds=cache_ttl)
        logger.info("JobSearchService initialized")

    async def search_jobs(
        self,
        db: AsyncSession,
        query: str,
        location: str,
        user_id: int,
        sources: Optional[List[str]] = None,
        employment_type: Optional[List[str]] = None,
        remote_only: bool = False,
        salary_min: Optional[int] = None,
        use_cache: bool = True,
        **kwargs,
    ) -> List[Job]:
        """
        Search for jobs and return normalized, deduplicated results.

        Args:
            db: Database session
            query: Job title or keywords
            location: Geographic location
            user_id: User performing the search
            sources: List of job sources to search
            employment_type: Filter by employment types
            remote_only: Filter for remote positions only
            salary_min: Minimum salary filter
            use_cache: Whether to use cached results
            **kwargs: Additional search parameters

        Returns:
            List of Job objects (may not be persisted yet)
        """
        cache_key = self._generate_cache_key(
            query, location, sources, employment_type, remote_only, salary_min
        )

        # Check cache
        if use_cache:
            cached_results = self.cache.get(cache_key)
            if cached_results:
                logger.info(f"Returning {len(cached_results)} cached results")
                return cached_results

        logger.info(
            f"Searching jobs: query='{query}', location='{location}', "
            f"sources={sources}, remote_only={remote_only}"
        )

        try:
            # Search using JobSpy client
            raw_jobs = await self.jobspy_client.search(
                query=query,
                location=location,
                sources=sources,
                employment_type=employment_type,
                remote_only=remote_only,
                salary_min=salary_min,
                **kwargs,
            )

            # Normalize jobs
            normalized_jobs = []
            for raw_job in raw_jobs:
                source = raw_job.get("source", "unknown")
                normalized = self.jobspy_client.normalize_job_data(raw_job, source)
                if normalized:
                    normalized_jobs.append(normalized)

            logger.info(f"Normalized {len(normalized_jobs)} jobs")

            # Deduplicate
            unique_jobs = await self._deduplicate_jobs(db, normalized_jobs)
            logger.info(f"Deduplicated to {len(unique_jobs)} unique jobs")

            # Create Job objects (not persisted yet)
            job_objects = []
            for job_data in unique_jobs:
                try:
                    job_obj = await self._create_job_object(db, job_data)
                    if job_obj:
                        job_objects.append(job_obj)
                except Exception as e:
                    logger.error(f"Error creating job object: {e}")
                    continue

            # Log search query
            await self._log_search_query(
                db, user_id, query, location, len(job_objects), sources
            )

            # Cache results
            if use_cache:
                self.cache.set(cache_key, job_objects)

            logger.info(f"Search complete: returning {len(job_objects)} jobs")
            return job_objects

        except Exception as e:
            logger.error(f"Job search failed: {e}")
            raise

    async def _create_job_object(
        self, db: AsyncSession, job_data: Dict[str, Any]
    ) -> Optional[Job]:
        """
        Create Job object from normalized data.

        Args:
            db: Database session
            job_data: Normalized job data

        Returns:
            Job object (not persisted)
        """
        try:
            # Get or create company
            company = await self._get_or_create_company(
                db, job_data.get("company", "Unknown Company")
            )

            # Parse employment type
            emp_type_str = job_data.get("employment_type", "full_time")
            try:
                employment_type = EmploymentType(emp_type_str)
            except ValueError:
                employment_type = EmploymentType.FULL_TIME

            # Parse remote policy
            remote_str = job_data.get("remote_policy", "unknown")
            try:
                remote_policy = RemotePolicy(remote_str)
            except ValueError:
                remote_policy = RemotePolicy.UNKNOWN

            # Create Job object
            job = Job(
                company_id=company.id if company.id else 0,  # Will be set on persist
                title=job_data.get("title", "Untitled Position"),
                description=job_data.get("description", ""),
                location=job_data.get("location", "Not specified"),
                remote_policy=remote_policy,
                salary_min=job_data.get("salary_min"),
                salary_max=job_data.get("salary_max"),
                salary_currency=job_data.get("salary_currency", "USD"),
                employment_type=employment_type,
                source=job_data.get("source", "unknown"),
                source_id=job_data.get("source_id"),
                url=job_data.get("url", ""),
                posted_date=job_data.get("posted_date"),
                benefits=job_data.get("benefits"),
                is_active=True,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )

            # Store company object for relationship
            job.company = company

            return job

        except Exception as e:
            logger.error(f"Error creating job object: {e}")
            return None

    async def _get_or_create_company(
        self, db: AsyncSession, company_name: str
    ) -> Company:
        """
        Get existing company or create new one.

        Args:
            db: Database session
            company_name: Company name

        Returns:
            Company object
        """
        try:
            # Search for existing company (case-insensitive)
            result = await db.execute(
                select(Company).where(Company.name.ilike(company_name))
            )
            company = result.scalar_one_or_none()

            if company:
                logger.debug(f"Found existing company: {company_name}")
                return company

            # Create new company
            company = Company(
                name=company_name,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            db.add(company)
            await db.flush()  # Get ID without committing
            logger.debug(f"Created new company: {company_name}")
            return company

        except Exception as e:
            logger.error(f"Error getting/creating company: {e}")
            # Return a company object without ID (will handle on persist)
            return Company(
                name=company_name,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )

    async def _deduplicate_jobs(
        self, db: AsyncSession, jobs: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Remove duplicate jobs based on title, company, and location.

        Args:
            db: Database session
            jobs: List of normalized job dictionaries

        Returns:
            List of unique job dictionaries
        """
        seen_hashes: Set[str] = set()
        unique_jobs: List[Dict[str, Any]] = []

        for job in jobs:
            # Create hash from key fields
            job_hash = self._generate_job_hash(
                job.get("title", ""),
                job.get("company", ""),
                job.get("location", ""),
            )

            if job_hash not in seen_hashes:
                seen_hashes.add(job_hash)
                unique_jobs.append(job)
            else:
                logger.debug(f"Duplicate job found: {job.get('title')} at {job.get('company')}")

        # Also check against database for existing jobs
        unique_jobs = await self._filter_existing_jobs(db, unique_jobs)

        return unique_jobs

    def _generate_job_hash(self, title: str, company: str, location: str) -> str:
        """
        Generate hash for duplicate detection.

        Args:
            title: Job title
            company: Company name
            location: Job location

        Returns:
            Hash string
        """
        # Normalize strings
        normalized = f"{title.lower().strip()}|{company.lower().strip()}|{location.lower().strip()}"
        return hashlib.md5(normalized.encode()).hexdigest()

    async def _filter_existing_jobs(
        self, db: AsyncSession, jobs: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Filter out jobs that already exist in database.

        Args:
            db: Database session
            jobs: List of job dictionaries

        Returns:
            List of jobs not in database
        """
        if not jobs:
            return []

        try:
            # Build query to check for existing jobs
            # Check by source_id if available, otherwise by title+company
            conditions = []
            for job in jobs:
                if job.get("source_id"):
                    conditions.append(
                        and_(
                            Job.source == job.get("source"),
                            Job.source_id == job.get("source_id"),
                        )
                    )
                else:
                    conditions.append(
                        and_(
                            Job.title == job.get("title"),
                            Job.location == job.get("location"),
                        )
                    )

            if conditions:
                result = await db.execute(
                    select(Job.source_id, Job.title, Job.location).where(or_(*conditions))
                )
                existing = result.all()

                # Create set of existing job identifiers
                existing_ids = {
                    (row.source_id, row.title, row.location) for row in existing
                }

                # Filter out existing jobs
                new_jobs = [
                    job
                    for job in jobs
                    if (job.get("source_id"), job.get("title"), job.get("location"))
                    not in existing_ids
                ]

                logger.debug(f"Filtered {len(jobs) - len(new_jobs)} existing jobs from database")
                return new_jobs

            return jobs

        except Exception as e:
            logger.error(f"Error filtering existing jobs: {e}")
            return jobs

    async def save_job(self, db: AsyncSession, job: Job) -> Job:
        """
        Persist job to database.

        Args:
            db: Database session
            job: Job object to save

        Returns:
            Saved job with ID
        """
        try:
            db.add(job)
            await db.flush()
            await db.refresh(job)
            logger.info(f"Saved job: {job.title} at {job.company.name}")
            return job

        except Exception as e:
            logger.error(f"Error saving job: {e}")
            raise

    async def create_manual_job(
        self,
        db: AsyncSession,
        title: str,
        company_name: str,
        url: str,
        location: str = "Not specified",
        description: str = "",
        **optional_fields,
    ) -> Job:
        """
        Create job entry manually (user-provided).

        Args:
            db: Database session
            title: Job title
            company_name: Company name
            url: Job URL
            location: Job location
            description: Job description
            **optional_fields: Additional optional fields

        Returns:
            Created Job object
        """
        logger.info(f"Creating manual job entry: {title} at {company_name}")

        try:
            # Get or create company
            company = await self._get_or_create_company(db, company_name)

            # Parse optional fields
            emp_type_str = optional_fields.get("employment_type", "full_time")
            try:
                employment_type = EmploymentType(emp_type_str)
            except ValueError:
                employment_type = EmploymentType.FULL_TIME

            remote_str = optional_fields.get("remote_policy", "unknown")
            try:
                remote_policy = RemotePolicy(remote_str)
            except ValueError:
                remote_policy = RemotePolicy.UNKNOWN

            # Create job
            job = Job(
                company_id=company.id,
                title=title,
                description=description,
                location=location,
                remote_policy=remote_policy,
                salary_min=optional_fields.get("salary_min"),
                salary_max=optional_fields.get("salary_max"),
                salary_currency=optional_fields.get("salary_currency", "USD"),
                employment_type=employment_type,
                source="manual",
                url=url,
                posted_date=optional_fields.get("posted_date", datetime.now(timezone.utc)),
                is_active=True,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )
            job.company = company

            db.add(job)
            await db.flush()
            await db.refresh(job)

            logger.info(f"Manual job created: {job.id}")
            return job

        except Exception as e:
            logger.error(f"Error creating manual job: {e}")
            raise

    async def _log_search_query(
        self,
        db: AsyncSession,
        user_id: int,
        query: str,
        location: str,
        results_count: int,
        sources: Optional[List[str]],
    ) -> None:
        """
        Log search query to database.

        Args:
            db: Database session
            user_id: User who performed search
            query: Search query
            location: Search location
            results_count: Number of results found
            sources: Sources searched
        """
        try:
            search_query = SearchQuery(
                user_id=user_id,
                query=query,
                location=location,
                filters={"sources": sources} if sources else None,
                results_count=results_count,
                source="api",
                created_at=datetime.now(timezone.utc),
            )
            db.add(search_query)
            await db.flush()
            logger.debug(f"Logged search query for user {user_id}")

        except Exception as e:
            logger.error(f"Error logging search query: {e}")
            # Don't fail the search if logging fails

    def _generate_cache_key(
        self,
        query: str,
        location: str,
        sources: Optional[List[str]],
        employment_type: Optional[List[str]],
        remote_only: bool,
        salary_min: Optional[int],
    ) -> str:
        """Generate cache key from search parameters."""
        parts = [
            query.lower(),
            location.lower(),
            "|".join(sorted(sources or [])),
            "|".join(sorted(employment_type or [])),
            str(remote_only),
            str(salary_min or ""),
        ]
        return hashlib.md5("|".join(parts).encode()).hexdigest()
