"""
Pydantic schemas for job-related API endpoints.

These schemas define request and response models for job search and management.
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class EmploymentTypeEnum(str, Enum):
    """Employment type options."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"


class RemotePolicyEnum(str, Enum):
    """Remote work policy options."""

    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"
    UNKNOWN = "unknown"


class JobSearchRequest(BaseModel):
    """Request model for job search."""

    query: str = Field(..., min_length=1, max_length=500, description="Job title or keywords")
    location: str = Field(..., min_length=1, max_length=255, description="Geographic location")
    sources: list[str] | None = Field(
        None, description="Job sources to search (linkedin, indeed, glassdoor, etc.)"
    )
    employment_type: list[EmploymentTypeEnum] | None = Field(
        None, description="Filter by employment types"
    )
    remote_only: bool = Field(False, description="Filter for remote positions only")
    salary_min: int | None = Field(None, ge=0, description="Minimum salary filter")
    max_results: int = Field(20, ge=1, le=100, description="Maximum results to return")

    class Config:
        json_schema_extra = {
            "example": {
                "query": "Python Developer",
                "location": "San Francisco, CA",
                "sources": ["linkedin", "indeed"],
                "employment_type": ["full_time"],
                "remote_only": False,
                "salary_min": 100000,
                "max_results": 20,
            }
        }


class CompanyResponse(BaseModel):
    """Response model for company information."""

    id: int
    name: str
    website: str | None = None
    logo_url: str | None = None
    industry: str | None = None
    location: str | None = None

    class Config:
        from_attributes = True


class JobResponse(BaseModel):
    """Response model for job listing."""

    id: int
    title: str
    company: CompanyResponse
    location: str
    remote_policy: RemotePolicyEnum
    salary_min: int | None = None
    salary_max: int | None = None
    salary_currency: str
    employment_type: EmploymentTypeEnum
    source: str
    url: str
    posted_date: datetime | None = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


class JobDetailResponse(JobResponse):
    """Detailed response model for single job."""

    description: str
    benefits: list[str] | None = None
    requirements_parsed: dict | None = None
    source_id: str | None = None
    updated_at: datetime

    class Config:
        from_attributes = True


class JobSearchResponse(BaseModel):
    """Response model for job search results."""

    jobs: list[JobResponse]
    total: int
    page: int = 1
    per_page: int = 20
    search_query: str
    search_location: str

    class Config:
        json_schema_extra = {
            "example": {
                "jobs": [],
                "total": 42,
                "page": 1,
                "per_page": 20,
                "search_query": "Python Developer",
                "search_location": "San Francisco, CA",
            }
        }


class CreateManualJobRequest(BaseModel):
    """Request model for manually creating a job entry."""

    title: str = Field(..., min_length=1, max_length=255)
    company_name: str = Field(..., min_length=1, max_length=255)
    url: str = Field(..., description="Job posting URL")
    location: str = Field(default="Not specified", max_length=255)
    description: str = Field(default="", description="Job description")
    employment_type: EmploymentTypeEnum = Field(default=EmploymentTypeEnum.FULL_TIME)
    remote_policy: RemotePolicyEnum = Field(default=RemotePolicyEnum.UNKNOWN)
    salary_min: int | None = Field(None, ge=0)
    salary_max: int | None = Field(None, ge=0)
    salary_currency: str = Field(default="USD", max_length=3)
    posted_date: datetime | None = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Senior Software Engineer",
                "company_name": "Tech Corp",
                "url": "https://example.com/careers/123",
                "location": "San Francisco, CA",
                "description": "Great opportunity!",
                "employment_type": "full_time",
                "remote_policy": "hybrid",
                "salary_min": 150000,
                "salary_max": 200000,
            }
        }


class JobListFilters(BaseModel):
    """Filters for listing jobs."""

    company_id: int | None = None
    location: str | None = None
    employment_type: EmploymentTypeEnum | None = None
    remote_policy: RemotePolicyEnum | None = None
    min_salary: int | None = None
    is_active: bool = True
    source: str | None = None
