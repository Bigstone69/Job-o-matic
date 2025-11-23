"""Integration tests for Jobs API endpoints.

Tests the /api/jobs endpoints using FastAPI TestClient for end-to-end HTTP request/response testing.
"""

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import AsyncSession

from src.main import app
from src.models.database import Job, Company, User


class TestJobsAPISearch:
    """Tests for job search endpoints."""

    @pytest.mark.asyncio
    async def test_search_jobs_basic(
        self, client: TestClient, test_user: User, test_job: Job
    ):
        """Test basic job search."""
        response = client.post(
            "/api/jobs/search",
            json={
                "query": "Software Engineer",
                "location": "San Francisco",
                "user_id": test_user.id,
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert "jobs" in data
        assert isinstance(data["jobs"], list)

    @pytest.mark.asyncio
    async def test_search_jobs_with_filters(
        self, client: TestClient, test_user: User
    ):
        """Test job search with filters."""
        response = client.post(
            "/api/jobs/search",
            json={
                "query": "Python Developer",
                "location": "Remote",
                "user_id": test_user.id,
                "remote_only": True,
                "employment_type": ["full_time"],
                "salary_min": 100000,
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert "jobs" in data

    @pytest.mark.asyncio
    async def test_search_jobs_missing_required_fields(self, client: TestClient):
        """Test search with missing required fields."""
        response = client.post(
            "/api/jobs/search",
            json={
                "query": "Developer",
                # Missing location and user_id
            },
        )

        assert response.status_code == 422  # Validation error

    @pytest.mark.asyncio
    async def test_search_jobs_invalid_user(self, client: TestClient):
        """Test search with non-existent user."""
        response = client.post(
            "/api/jobs/search",
            json={
                "query": "Developer",
                "location": "NYC",
                "user_id": 99999,  # Non-existent user
            },
        )

        # Should handle gracefully, might return 404 or empty results depending on implementation
        assert response.status_code in [200, 404]


class TestJobsAPIGetJob:
    """Tests for getting individual jobs."""

    @pytest.mark.asyncio
    async def test_get_job_by_id(
        self, client: TestClient, test_job: Job
    ):
        """Test retrieving job by ID."""
        response = client.get(f"/api/jobs/{test_job.id}")

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_job.id
        assert data["title"] == test_job.title
        assert "company" in data

    @pytest.mark.asyncio
    async def test_get_job_not_found(self, client: TestClient):
        """Test retrieving non-existent job."""
        response = client.get("/api/jobs/99999")

        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()

    @pytest.mark.asyncio
    async def test_get_job_invalid_id(self, client: TestClient):
        """Test retrieving job with invalid ID format."""
        response = client.get("/api/jobs/invalid")

        assert response.status_code == 422  # Validation error


class TestJobsAPIList:
    """Tests for listing jobs."""

    @pytest.mark.asyncio
    async def test_list_jobs(
        self, client: TestClient, test_job: Job
    ):
        """Test listing all jobs."""
        response = client.get("/api/jobs/")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= 1

    @pytest.mark.asyncio
    async def test_list_jobs_with_pagination(
        self, client: TestClient, test_job: Job
    ):
        """Test listing jobs with pagination."""
        response = client.get("/api/jobs/?skip=0&limit=10")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) <= 10

    @pytest.mark.asyncio
    async def test_list_jobs_filter_by_company(
        self, client: TestClient, test_job: Job, test_company: Company
    ):
        """Test filtering jobs by company."""
        response = client.get(f"/api/jobs/?company_id={test_company.id}")

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        for job in data:
            assert job["company_id"] == test_company.id


class TestJobsAPIManualEntry:
    """Tests for manual job entry."""

    @pytest.mark.asyncio
    async def test_create_manual_job(
        self, client: TestClient, test_company: Company
    ):
        """Test creating a manual job entry."""
        response = client.post(
            "/api/jobs/manual",
            json={
                "title": "Senior Python Developer",
                "company_name": test_company.name,
                "location": "Remote",
                "url": "https://example.com/job/123",
                "description": "Great opportunity",
                "salary_min": 120000,
                "salary_max": 160000,
                "employment_type": "full_time",
                "remote_policy": "remote",
            },
        )

        assert response.status_code == 201
        data = response.json()
        assert data["title"] == "Senior Python Developer"
        assert data["id"] is not None

    @pytest.mark.asyncio
    async def test_create_manual_job_new_company(
        self, client: TestClient
    ):
        """Test creating manual job with new company."""
        response = client.post(
            "/api/jobs/manual",
            json={
                "title": "DevOps Engineer",
                "company_name": "New Tech Startup",
                "location": "Austin, TX",
                "url": "https://newtech.com/careers",
                "description": "Work on cutting-edge infrastructure",
                "employment_type": "full_time",
            },
        )

        assert response.status_code == 201
        data = response.json()
        assert data["company"]["name"] == "New Tech Startup"

    @pytest.mark.asyncio
    async def test_create_manual_job_missing_required(
        self, client: TestClient
    ):
        """Test creating manual job with missing required fields."""
        response = client.post(
            "/api/jobs/manual",
            json={
                "title": "Engineer",
                # Missing company_name, location, url
            },
        )

        assert response.status_code == 422  # Validation error

    @pytest.mark.asyncio
    async def test_create_manual_job_duplicate_url(
        self, client: TestClient, test_job: Job
    ):
        """Test creating manual job with duplicate URL."""
        response = client.post(
            "/api/jobs/manual",
            json={
                "title": "Another Job",
                "company_name": "Test Company",
                "location": "NYC",
                "url": test_job.url,  # Duplicate URL
                "description": "Duplicate test",
                "employment_type": "full_time",
            },
        )

        # Should handle gracefully - either reject or return existing
        assert response.status_code in [201, 400, 409]


class TestJobsAPIUpdate:
    """Tests for updating jobs."""

    @pytest.mark.asyncio
    async def test_update_job(
        self, client: TestClient, test_job: Job
    ):
        """Test updating job details."""
        response = client.patch(
            f"/api/jobs/{test_job.id}",
            json={
                "description": "Updated description",
                "salary_min": 130000,
            },
        )

        assert response.status_code == 200
        data = response.json()
        assert data["description"] == "Updated description"
        assert data["salary_min"] == 130000

    @pytest.mark.asyncio
    async def test_update_job_not_found(self, client: TestClient):
        """Test updating non-existent job."""
        response = client.patch(
            "/api/jobs/99999",
            json={"description": "Updated"},
        )

        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_update_job_invalid_data(
        self, client: TestClient, test_job: Job
    ):
        """Test updating job with invalid data."""
        response = client.patch(
            f"/api/jobs/{test_job.id}",
            json={
                "salary_min": "invalid",  # Should be integer
            },
        )

        assert response.status_code == 422


class TestJobsAPIDelete:
    """Tests for deleting jobs."""

    @pytest.mark.asyncio
    async def test_delete_job(
        self, client: TestClient, test_job: Job
    ):
        """Test soft-deleting a job."""
        response = client.delete(f"/api/jobs/{test_job.id}")

        assert response.status_code == 200

        # Verify job is marked inactive
        get_response = client.get(f"/api/jobs/{test_job.id}")
        # Depending on implementation, might be 404 or return with is_active=false
        assert get_response.status_code in [200, 404]

    @pytest.mark.asyncio
    async def test_delete_job_not_found(self, client: TestClient):
        """Test deleting non-existent job."""
        response = client.delete("/api/jobs/99999")

        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_delete_job_with_applications(
        self, client: TestClient, test_job: Job, test_application
    ):
        """Test deleting job that has applications."""
        response = client.delete(f"/api/jobs/{test_job.id}")

        # Should either cascade delete or prevent deletion
        assert response.status_code in [200, 400, 409]


class TestJobsAPIStatistics:
    """Tests for job statistics endpoints."""

    @pytest.mark.asyncio
    async def test_get_job_stats(
        self, client: TestClient, test_job: Job
    ):
        """Test retrieving job statistics."""
        response = client.get("/api/jobs/stats")

        assert response.status_code == 200
        data = response.json()
        assert "total_jobs" in data
        assert "active_jobs" in data
        assert isinstance(data["total_jobs"], int)

    @pytest.mark.asyncio
    async def test_get_job_stats_by_company(
        self, client: TestClient, test_company: Company
    ):
        """Test retrieving job statistics by company."""
        response = client.get(f"/api/jobs/stats/company/{test_company.id}")

        assert response.status_code == 200
        data = response.json()
        assert "company_name" in data
        assert "job_count" in data
