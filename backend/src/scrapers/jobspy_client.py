"""
JobSpy client for job search across multiple platforms.

This module provides a wrapper around the JobSpy library (or API)
to search for jobs from LinkedIn, Indeed, Glassdoor, and other sources.
"""

import asyncio
import logging
from datetime import datetime
from functools import wraps
from typing import Any

logger = logging.getLogger(__name__)


def async_retry(max_retries: int = 3, delay: float = 1.0):
    """Decorator for retrying async functions."""

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return await func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {e}. Retrying..."
                    )
                    await asyncio.sleep(delay * (attempt + 1))
            return None

        return wrapper

    return decorator


class JobSpyClient:
    """
    Client for searching jobs using JobSpy library/API.

    This client provides async methods to search jobs from multiple sources
    including LinkedIn, Indeed, Glassdoor, ZipRecruiter, and Google.
    """

    def __init__(
        self,
        rate_limit_delay: float = 2.0,
        max_results: int = 100,
        timeout: int = 30,
    ):
        """
        Initialize JobSpy client.

        Args:
            rate_limit_delay: Delay between requests in seconds
            max_results: Maximum number of results to return
            timeout: Request timeout in seconds
        """
        self.rate_limit_delay = rate_limit_delay
        self.max_results = max_results
        self.timeout = timeout
        logger.info(f"JobSpyClient initialized with max_results={max_results}")

    @async_retry(max_retries=3, delay=2.0)
    async def search(
        self,
        query: str,
        location: str,
        sources: list[str] | None = None,
        employment_type: list[str] | None = None,
        remote_only: bool = False,
        salary_min: int | None = None,
        **kwargs,
    ) -> list[dict[str, Any]]:
        """
        Search for jobs across multiple platforms.

        Args:
            query: Job title or keywords (e.g., "Python Developer")
            location: Geographic location (e.g., "San Francisco, CA")
            sources: List of sources to search (linkedin, indeed, glassdoor, etc.)
                    If None, searches all sources
            employment_type: List of employment types (full_time, part_time, contract, etc.)
            remote_only: Filter for remote positions only
            salary_min: Minimum salary filter
            **kwargs: Additional filter parameters

        Returns:
            List of job dictionaries with normalized structure

        Raises:
            Exception: If search fails after retries
        """
        logger.info(
            f"Searching jobs: query='{query}', location='{location}', "
            f"sources={sources}, remote_only={remote_only}"
        )

        # Default to all sources if not specified
        if sources is None:
            sources = ["linkedin", "indeed", "glassdoor", "zip_recruiter"]

        try:
            # In a real implementation, this would call the JobSpy library
            # For now, we'll simulate the structure
            jobs = await self._execute_search(
                query=query,
                location=location,
                sources=sources,
                employment_type=employment_type,
                remote_only=remote_only,
                salary_min=salary_min,
                **kwargs,
            )

            logger.info(f"Found {len(jobs)} jobs from {sources}")
            return jobs

        except Exception as e:
            logger.error(f"Job search failed: {e}")
            raise

    async def _execute_search(
        self,
        query: str,
        location: str,
        sources: list[str],
        employment_type: list[str] | None,
        remote_only: bool,
        salary_min: int | None,
        **kwargs,
    ) -> list[dict[str, Any]]:
        """
        Execute the actual search (internal method).

        This method would integrate with the actual JobSpy library or API.
        For demonstration, it returns a structured format.
        """
        # Simulate async operation
        await asyncio.sleep(self.rate_limit_delay)

        # In production, this would be:
        # from jobspy import scrape_jobs
        # jobs = scrape_jobs(
        #     site_name=sources,
        #     search_term=query,
        #     location=location,
        #     results_wanted=self.max_results,
        #     hours_old=72,
        #     country_indeed='USA'
        # )

        # For now, return empty list (will be populated when JobSpy is integrated)
        # In Phase 2 review, we'll add mock data or real integration
        logger.debug(f"Executing search for {query} in {location}")
        return []

    async def get_job_details(self, job_id: str, source: str) -> dict[str, Any] | None:
        """
        Get detailed information about a specific job.

        Args:
            job_id: The job ID from the source platform
            source: The source platform (linkedin, indeed, etc.)

        Returns:
            Detailed job information or None if not found
        """
        logger.info(f"Fetching job details: id={job_id}, source={source}")

        try:
            await asyncio.sleep(self.rate_limit_delay)

            # In production, this would fetch from the specific source
            logger.debug(f"Fetched details for job {job_id} from {source}")
            return None

        except Exception as e:
            logger.error(f"Failed to fetch job details: {e}")
            return None

    def normalize_job_data(self, raw_job: dict[str, Any], source: str) -> dict[str, Any]:
        """
        Normalize job data from different sources into a standard format.

        Args:
            raw_job: Raw job data from source
            source: Source platform name

        Returns:
            Normalized job dictionary
        """
        try:
            # Standard normalized format
            normalized = {
                "title": self._extract_field(raw_job, ["title", "job_title", "position"]),
                "company": self._extract_field(raw_job, ["company", "company_name", "employer"]),
                "location": self._extract_field(raw_job, ["location", "job_location", "city"]),
                "description": self._extract_field(
                    raw_job, ["description", "job_description", "details"]
                ),
                "url": self._extract_field(raw_job, ["url", "job_url", "link"]),
                "posted_date": self._parse_date(
                    self._extract_field(raw_job, ["posted", "date_posted", "published"])
                ),
                "salary_min": self._extract_salary(raw_job, "min"),
                "salary_max": self._extract_salary(raw_job, "max"),
                "salary_currency": self._extract_field(raw_job, ["currency"], default="USD"),
                "employment_type": self._normalize_employment_type(
                    self._extract_field(raw_job, ["type", "employment_type", "job_type"])
                ),
                "remote_policy": self._normalize_remote_policy(
                    self._extract_field(raw_job, ["remote", "work_from_home", "location"])
                ),
                "source": source,
                "source_id": self._extract_field(raw_job, ["id", "job_id"]),
                "benefits": self._extract_list_field(raw_job, ["benefits", "perks"]),
            }

            return {k: v for k, v in normalized.items() if v is not None}

        except Exception as e:
            logger.error(f"Error normalizing job data: {e}")
            return {}

    def _extract_field(self, data: dict, field_names: list[str], default: Any = None) -> Any:
        """Extract field from data using multiple possible field names."""
        for field in field_names:
            if field in data and data[field]:
                return data[field]
        return default

    def _extract_list_field(self, data: dict, field_names: list[str]) -> list[str] | None:
        """Extract list field from data."""
        for field in field_names:
            if field in data and isinstance(data[field], list):
                return data[field]
        return None

    def _parse_date(self, date_str: str | None) -> datetime | None:
        """Parse date string to datetime object."""
        if not date_str:
            return None

        try:
            # Handle various date formats
            # In production, use dateutil.parser
            return datetime.fromisoformat(str(date_str).replace("Z", "+00:00"))
        except Exception as e:
            logger.debug(f"Could not parse date '{date_str}': {e}")
            return None

    def _extract_salary(self, data: dict, salary_type: str) -> int | None:
        """Extract min or max salary from various formats."""
        salary_fields = ["salary", "compensation", "pay"]

        for field in salary_fields:
            if field in data:
                salary_data = data[field]
                if isinstance(salary_data, dict):
                    if salary_type == "min" and "min" in salary_data:
                        return int(salary_data["min"])
                    if salary_type == "max" and "max" in salary_data:
                        return int(salary_data["max"])
                elif isinstance(salary_data, (int, float)):
                    return int(salary_data)

        return None

    def _normalize_employment_type(self, emp_type: str | None) -> str:
        """Normalize employment type to standard values."""
        if not emp_type:
            return "full_time"

        emp_type_lower = str(emp_type).lower()

        if any(x in emp_type_lower for x in ["full", "fulltime", "full-time"]):
            return "full_time"
        elif any(x in emp_type_lower for x in ["part", "parttime", "part-time"]):
            return "part_time"
        elif any(x in emp_type_lower for x in ["contract", "contractor"]):
            return "contract"
        elif any(x in emp_type_lower for x in ["temp", "temporary"]):
            return "temporary"
        elif any(x in emp_type_lower for x in ["intern", "internship"]):
            return "internship"
        else:
            return "full_time"

    def _normalize_remote_policy(self, location_or_remote: str | None) -> str:
        """Determine remote policy from location or remote field."""
        if not location_or_remote:
            return "unknown"

        text_lower = str(location_or_remote).lower()

        if any(x in text_lower for x in ["remote", "work from home", "wfh", "anywhere"]):
            return "remote"
        elif any(x in text_lower for x in ["hybrid"]):
            return "hybrid"
        elif any(x in text_lower for x in ["onsite", "on-site", "office"]):
            return "onsite"
        else:
            return "unknown"


# Singleton instance (optional, for shared rate limiting)
_jobspy_client_instance: JobSpyClient | None = None


def get_jobspy_client() -> JobSpyClient:
    """Get or create singleton JobSpy client instance."""
    global _jobspy_client_instance
    if _jobspy_client_instance is None:
        _jobspy_client_instance = JobSpyClient()
    return _jobspy_client_instance
