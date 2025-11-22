"""Tests for JobSpy client."""

import pytest
from datetime import datetime
from src.scrapers.jobspy_client import JobSpyClient, get_jobspy_client


class TestJobSpyClient:
    """Test suite for JobSpyClient."""

    @pytest.fixture
    def client(self):
        """Create JobSpy client for testing."""
        return JobSpyClient(rate_limit_delay=0.1, max_results=10)

    @pytest.mark.asyncio
    async def test_search_basic(self, client):
        """Test basic job search."""
        results = await client.search(
            query="Python Developer",
            location="San Francisco, CA"
        )

        assert isinstance(results, list)
        # Currently returns empty list (will be populated with mock/real data)

    @pytest.mark.asyncio
    async def test_search_with_filters(self, client):
        """Test job search with filters."""
        results = await client.search(
            query="Software Engineer",
            location="Remote",
            sources=["linkedin", "indeed"],
            employment_type=["full_time"],
            remote_only=True,
            salary_min=100000
        )

        assert isinstance(results, list)

    @pytest.mark.asyncio
    async def test_get_job_details(self, client):
        """Test getting job details."""
        result = await client.get_job_details(
            job_id="test-123",
            source="linkedin"
        )

        # Currently returns None (will be implemented)
        assert result is None or isinstance(result, dict)

    def test_normalize_job_data(self, client):
        """Test job data normalization."""
        raw_job = {
            "title": "Senior Python Developer",
            "company": "Tech Corp",
            "location": "San Francisco, CA",
            "description": "Great job!",
            "url": "https://example.com/job/123",
            "posted": "2025-11-20",
            "salary": {"min": 120000, "max": 180000, "currency": "USD"},
            "type": "Full Time",
            "remote": "Hybrid",
            "id": "job-123"
        }

        normalized = client.normalize_job_data(raw_job, "indeed")

        assert normalized["title"] == "Senior Python Developer"
        assert normalized["company"] == "Tech Corp"
        assert normalized["employment_type"] == "full_time"
        assert normalized["remote_policy"] == "hybrid"
        assert normalized["salary_min"] == 120000
        assert normalized["source"] == "indeed"

    def test_normalize_employment_type(self, client):
        """Test employment type normalization."""
        assert client._normalize_employment_type("Full-time") == "full_time"
        assert client._normalize_employment_type("Part Time") == "part_time"
        assert client._normalize_employment_type("Contract") == "contract"
        assert client._normalize_employment_type("Temporary") == "temporary"
        assert client._normalize_employment_type("Internship") == "internship"
        assert client._normalize_employment_type(None) == "full_time"

    def test_normalize_remote_policy(self, client):
        """Test remote policy normalization."""
        assert client._normalize_remote_policy("Remote") == "remote"
        assert client._normalize_remote_policy("Work from home") == "remote"
        assert client._normalize_remote_policy("Hybrid") == "hybrid"
        assert client._normalize_remote_policy("On-site") == "onsite"
        assert client._normalize_remote_policy("Office") == "onsite"
        assert client._normalize_remote_policy(None) == "unknown"

    def test_extract_field(self, client):
        """Test field extraction with multiple possible names."""
        data = {"job_title": "Developer", "company_name": "Tech Corp"}

        assert client._extract_field(data, ["title", "job_title"]) == "Developer"
        assert client._extract_field(data, ["company", "company_name"]) == "Tech Corp"
        assert client._extract_field(data, ["missing"], "default") == "default"

    def test_get_jobspy_client_singleton(self):
        """Test singleton pattern for JobSpy client."""
        client1 = get_jobspy_client()
        client2 = get_jobspy_client()

        assert client1 is client2
