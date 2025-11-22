"""
Unit tests for JobSearchService.

Tests cover:
- External job searching with mocked JobSpy
- Job creation and persistence
- Company management (get_or_create)
- Deduplication logic
- Cache functionality
- Manual job entry
"""

import pytest
from datetime import datetime, UTC
from unittest.mock import AsyncMock, MagicMock, patch
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.job_search_service import JobSearchService, JobCache
from src.models.database import Job, Company, EmploymentType, RemotePolicy


# ============================================================================
# Cache Tests
# ============================================================================


class TestJobCache:
    """Tests for JobCache functionality."""

    def test_cache_stores_and_retrieves_results(self):
        """Test that cache stores and retrieves results correctly."""
        cache = JobCache(ttl_seconds=300)
        key = "test_key"
        results = [MagicMock(spec=Job), MagicMock(spec=Job)]

        # Store results
        cache.set(key, results)

        # Retrieve results
        cached = cache.get(key)

        assert cached is not None
        assert len(cached) == 2
        assert cached == results

    def test_cache_returns_none_for_missing_key(self):
        """Test that cache returns None for non-existent keys."""
        cache = JobCache(ttl_seconds=300)

        result = cache.get("nonexistent_key")

        assert result is None

    def test_cache_expires_after_ttl(self):
        """Test that cache entries expire after TTL."""
        cache = JobCache(ttl_seconds=0)  # Expires immediately
        key = "test_key"
        results = [MagicMock(spec=Job)]

        cache.set(key, results)

        # Wait a bit for expiration (TTL=0 means expires immediately)
        import time
        time.sleep(0.1)

        # Should return None after expiration
        cached = cache.get(key)
        assert cached is None

    def test_cache_clear_removes_all_entries(self):
        """Test that clear() removes all cached entries."""
        cache = JobCache(ttl_seconds=300)

        cache.set("key1", [MagicMock(spec=Job)])
        cache.set("key2", [MagicMock(spec=Job)])

        cache.clear()

        assert cache.get("key1") is None
        assert cache.get("key2") is None


# ============================================================================
# Company Management Tests
# ============================================================================


class TestJobSearchServiceCompanyManagement:
    """Tests for company creation and lookup."""

    @pytest.mark.asyncio
    async def test_get_or_create_company_creates_new(self, db_session: AsyncSession):
        """Test creating a new company."""
        service = JobSearchService()
        company_name = "Test Company Inc"

        company = await service._get_or_create_company(db_session, company_name)

        assert company is not None
        assert company.id is not None
        assert company.name == company_name
        assert company.domain is None  # Domain extracted from name

    @pytest.mark.asyncio
    async def test_get_or_create_company_reuses_existing(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test that existing company is reused."""
        service = JobSearchService()

        # Try to create company with same name
        company = await service._get_or_create_company(db_session, test_company.name)

        assert company.id == test_company.id
        assert company.name == test_company.name

    @pytest.mark.asyncio
    async def test_get_or_create_company_case_insensitive(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test that company lookup is case-insensitive."""
        service = JobSearchService()

        # Try with different case
        company = await service._get_or_create_company(
            db_session, test_company.name.upper()
        )

        # Should find existing company
        assert company.id == test_company.id

    @pytest.mark.asyncio
    async def test_get_or_create_company_normalizes_whitespace(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test that company name whitespace is normalized."""
        service = JobSearchService()

        # Try with extra whitespace
        company = await service._get_or_create_company(
            db_session, f"  {test_company.name}  "
        )

        # Should find existing company (whitespace normalized)
        assert company.id == test_company.id


# ============================================================================
# Job Search Tests (with mocked JobSpy)
# ============================================================================


class TestJobSearchServiceSearch:
    """Tests for external job searching via JobSpy."""

    @pytest.mark.asyncio
    async def test_search_jobs_basic_query(self, db_session: AsyncSession, test_user):
        """Test basic job search with mocked JobSpy."""
        mock_jobspy = AsyncMock()
        mock_jobspy.search = AsyncMock(return_value=[
            {
                "title": "Software Engineer",
                "company": "Tech Corp",
                "location": "San Francisco, CA",
                "description": "Build great software",
                "url": "http://example.com/job1",
                "source": "indeed",
                "employment_type": "full_time",
            },
            {
                "title": "Python Developer",
                "company": "Another Co",
                "location": "New York, NY",
                "description": "Python development",
                "url": "http://example.com/job2",
                "source": "linkedin",
                "employment_type": "full_time",
            },
        ])
        mock_jobspy.normalize_job_data = MagicMock(side_effect=lambda x, source: x)

        service = JobSearchService(jobspy_client=mock_jobspy)

        results = await service.search_jobs(
            db=db_session,
            query="python developer",
            location="San Francisco",
            user_id=test_user.id,
            use_cache=False,  # Disable cache for testing
        )

        assert len(results) >= 2
        assert all(isinstance(job, Job) for job in results)
        # Verify JobSpy was called
        mock_jobspy.search.assert_called_once()

    @pytest.mark.asyncio
    async def test_search_jobs_uses_cache(self, db_session: AsyncSession, test_user):
        """Test that cache is used for repeated searches."""
        mock_jobspy = AsyncMock()
        mock_jobspy.search = AsyncMock(return_value=[
            {
                "title": "Engineer",
                "company": "Test Corp",
                "location": "SF",
                "url": "http://test.com/job1",
                "source": "indeed",
            }
        ])
        mock_jobspy.normalize_job_data = MagicMock(side_effect=lambda x, source: x)

        service = JobSearchService(jobspy_client=mock_jobspy, cache_ttl=300)

        # First search - should hit JobSpy
        results1 = await service.search_jobs(
            db=db_session,
            query="engineer",
            location="SF",
            user_id=test_user.id,
            use_cache=True,
        )

        # Second search with same params - should use cache
        results2 = await service.search_jobs(
            db=db_session,
            query="engineer",
            location="SF",
            user_id=test_user.id,
            use_cache=True,
        )

        # JobSpy should only be called once (second call used cache)
        assert mock_jobspy.search.call_count == 1
        assert len(results1) == len(results2)

    @pytest.mark.asyncio
    async def test_search_jobs_with_filters(self, db_session: AsyncSession, test_user):
        """Test job search with employment type and remote filters."""
        mock_jobspy = AsyncMock()
        mock_jobspy.search = AsyncMock(return_value=[
            {
                "title": "Remote Engineer",
                "company": "Remote Co",
                "location": "Remote",
                "url": "http://test.com/remote",
                "source": "indeed",
                "employment_type": "full_time",
                "remote": True,
            }
        ])
        mock_jobspy.normalize_job_data = MagicMock(side_effect=lambda x, source: x)

        service = JobSearchService(jobspy_client=mock_jobspy)

        results = await service.search_jobs(
            db=db_session,
            query="engineer",
            location="Remote",
            user_id=test_user.id,
            employment_type=["full_time"],
            remote_only=True,
            use_cache=False,
        )

        # Verify filters were passed to JobSpy
        call_kwargs = mock_jobspy.search.call_args.kwargs
        assert call_kwargs["employment_type"] == ["full_time"]
        assert call_kwargs["remote_only"] is True

    @pytest.mark.asyncio
    async def test_search_jobs_deduplicates_results(
        self, db_session: AsyncSession, test_user
    ):
        """Test that duplicate jobs are filtered out."""
        duplicate_job = {
            "title": "Engineer",
            "company": "Test Corp",
            "location": "SF",
            "url": "http://test.com/duplicate",
            "source": "indeed",
        }

        mock_jobspy = AsyncMock()
        mock_jobspy.search = AsyncMock(return_value=[
            duplicate_job,
            duplicate_job,  # Same job twice
            {**duplicate_job, "source": "linkedin"},  # Same URL, different source
        ])
        mock_jobspy.normalize_job_data = MagicMock(side_effect=lambda x, source: x)

        service = JobSearchService(jobspy_client=mock_jobspy)

        results = await service.search_jobs(
            db=db_session,
            query="engineer",
            location="SF",
            user_id=test_user.id,
            use_cache=False,
        )

        # Should only return one job (duplicates removed)
        assert len(results) == 1

    @pytest.mark.asyncio
    async def test_search_jobs_handles_jobspy_errors(
        self, db_session: AsyncSession, test_user
    ):
        """Test that JobSpy errors are properly raised."""
        mock_jobspy = AsyncMock()
        mock_jobspy.search = AsyncMock(side_effect=Exception("JobSpy API error"))

        service = JobSearchService(jobspy_client=mock_jobspy)

        with pytest.raises(Exception, match="JobSpy API error"):
            await service.search_jobs(
                db=db_session,
                query="engineer",
                location="SF",
                user_id=test_user.id,
                use_cache=False,
            )


# ============================================================================
# Job Creation and Persistence Tests
# ============================================================================


class TestJobSearchServiceJobManagement:
    """Tests for job creation and persistence."""

    @pytest.mark.asyncio
    async def test_create_manual_job_success(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test creating a manual job entry."""
        service = JobSearchService()

        job = await service.create_manual_job(
            db=db_session,
            title="Manual Job Entry",
            company_id=test_company.id,
            location="Remote",
            description="Test description",
            url="http://company.com/careers/123",
            salary_min=80000,
            salary_max=120000,
            employment_type=EmploymentType.FULL_TIME,
            remote_policy=RemotePolicy.REMOTE,
        )

        assert job.id is not None
        assert job.title == "Manual Job Entry"
        assert job.company_id == test_company.id
        assert job.location == "Remote"
        assert job.salary_min == 80000
        assert job.salary_max == 120000
        assert job.employment_type == EmploymentType.FULL_TIME
        assert job.remote_policy == RemotePolicy.REMOTE

    @pytest.mark.asyncio
    async def test_create_manual_job_invalid_company_raises_error(
        self, db_session: AsyncSession
    ):
        """Test that invalid company ID raises ValueError."""
        service = JobSearchService()

        with pytest.raises(ValueError, match="Company .* not found"):
            await service.create_manual_job(
                db=db_session,
                title="Test Job",
                company_id=99999,  # Non-existent company
                location="Remote",
            )

    @pytest.mark.asyncio
    async def test_save_job_persists_to_database(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test that save_job persists job to database."""
        service = JobSearchService()

        # Create a non-persisted job object
        job = Job(
            title="Test Job",
            company_id=test_company.id,
            location="San Francisco, CA",
            description="Test description",
        )

        # Save to database
        saved_job = await service.save_job(db_session, job)

        assert saved_job.id is not None
        assert saved_job.title == "Test Job"
        assert saved_job.company_id == test_company.id

    @pytest.mark.asyncio
    async def test_save_job_sets_timestamps(
        self, db_session: AsyncSession, test_company: Company
    ):
        """Test that save_job sets created_at and updated_at timestamps."""
        service = JobSearchService()

        job = Job(
            title="Test Job",
            company_id=test_company.id,
            location="Remote",
        )

        saved_job = await service.save_job(db_session, job)

        assert saved_job.created_at is not None
        assert saved_job.updated_at is not None
        assert isinstance(saved_job.created_at, datetime)
        assert isinstance(saved_job.updated_at, datetime)


# ============================================================================
# Deduplication Tests
# ============================================================================


class TestJobSearchServiceDeduplication:
    """Tests for job deduplication logic."""

    @pytest.mark.asyncio
    async def test_deduplicate_jobs_removes_duplicate_urls(self, db_session: AsyncSession):
        """Test that jobs with duplicate URLs are removed."""
        service = JobSearchService()

        jobs_data = [
            {"title": "Job 1", "company": "Co A", "url": "http://test.com/job1"},
            {"title": "Job 2", "company": "Co B", "url": "http://test.com/job1"},  # Duplicate URL
            {"title": "Job 3", "company": "Co C", "url": "http://test.com/job2"},
        ]

        unique_jobs = await service._deduplicate_jobs(db_session, jobs_data)

        # Should only have 2 unique jobs (by URL)
        assert len(unique_jobs) == 2
        urls = {job["url"] for job in unique_jobs}
        assert "http://test.com/job1" in urls
        assert "http://test.com/job2" in urls

    @pytest.mark.asyncio
    async def test_deduplicate_jobs_handles_missing_urls(self, db_session: AsyncSession):
        """Test deduplication when some jobs don't have URLs."""
        service = JobSearchService()

        jobs_data = [
            {"title": "Job 1", "company": "Co A"},  # No URL
            {"title": "Job 2", "company": "Co B", "url": "http://test.com/job1"},
            {"title": "Job 3", "company": "Co C"},  # No URL
        ]

        unique_jobs = await service._deduplicate_jobs(db_session, jobs_data)

        # Jobs without URLs should be kept (can't deduplicate)
        assert len(unique_jobs) >= 2

    @pytest.mark.asyncio
    async def test_filter_existing_jobs_removes_already_saved(
        self, db_session: AsyncSession, test_job: Job
    ):
        """Test that jobs already in database are filtered out."""
        service = JobSearchService()

        jobs_data = [
            {"title": "New Job", "company": "New Co", "url": "http://test.com/new"},
            {"title": test_job.title, "company": "Test", "url": test_job.url},  # Exists in DB
        ]

        # Filter out existing jobs
        new_jobs = await service._filter_existing_jobs(db_session, jobs_data)

        # Should only have the new job
        assert len(new_jobs) == 1
        assert new_jobs[0]["url"] == "http://test.com/new"
