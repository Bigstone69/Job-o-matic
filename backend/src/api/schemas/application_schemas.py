"""
Pydantic schemas for application-related API endpoints.

These schemas define request and response models for application tracking and management.
"""

from datetime import datetime

from pydantic import BaseModel, Field

from src.api.schemas.job_schemas import JobResponse
from src.models.database import ApplicationStatus

# Request Schemas


class CreateApplicationRequest(BaseModel):
    """Request model for creating an application."""

    job_id: int = Field(..., gt=0, description="ID of the job being applied to")
    status: ApplicationStatus = Field(
        default=ApplicationStatus.DRAFT,
        description="Initial application status",
    )
    notes: str | None = Field(None, max_length=2000, description="Application notes")
    resume_version: str | None = Field(None, max_length=255, description="Resume version used")
    cover_letter_id: int | None = Field(None, description="ID of associated cover letter")
    applied_date: datetime | None = Field(None, description="Date applied")
    interview_date: datetime | None = Field(None, description="Interview date")
    offer_deadline: datetime | None = Field(None, description="Offer deadline date")
    salary_offered: int | None = Field(None, ge=0, description="Salary offered")

    class Config:
        json_schema_extra = {
            "example": {
                "job_id": 123,
                "status": "draft",
                "notes": "Tailored resume for this position",
                "resume_version": "Software_Engineer_v2.pdf",
            }
        }


class UpdateApplicationRequest(BaseModel):
    """Request model for updating an application."""

    notes: str | None = Field(None, max_length=2000)
    resume_version: str | None = Field(None, max_length=255)
    cover_letter_id: int | None = None
    applied_date: datetime | None = None
    interview_date: datetime | None = None
    offer_deadline: datetime | None = None
    salary_offered: int | None = Field(None, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "notes": "Updated notes after phone screening",
                "interview_date": "2025-12-01T14:00:00Z",
            }
        }


class UpdateStatusRequest(BaseModel):
    """Request model for updating application status."""

    status: ApplicationStatus = Field(..., description="New application status")
    notes: str | None = Field(None, max_length=500, description="Notes about the status change")

    class Config:
        json_schema_extra = {
            "example": {
                "status": "interview",
                "notes": "Scheduled for technical interview next week",
            }
        }


# Response Schemas


class StatusHistoryResponse(BaseModel):
    """Response model for status history entry."""

    id: int
    old_status: ApplicationStatus | None = None
    new_status: ApplicationStatus
    notes: str | None = None
    created_at: datetime

    class Config:
        from_attributes = True


class ApplicationResponse(BaseModel):
    """Response model for application listing."""

    id: int
    job: JobResponse
    status: ApplicationStatus
    applied_date: datetime | None = None
    interview_date: datetime | None = None
    offer_deadline: datetime | None = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ApplicationDetailResponse(ApplicationResponse):
    """Detailed response model for single application."""

    notes: str | None = None
    resume_version: str | None = None
    cover_letter_id: int | None = None
    salary_offered: int | None = None
    status_history: list[StatusHistoryResponse] = []

    class Config:
        from_attributes = True


class ApplicationStatsResponse(BaseModel):
    """Response model for application statistics."""

    total: int = Field(..., description="Total number of applications")
    active: int = Field(..., description="Active applications (non-terminal states)")
    by_status: dict[str, int] = Field(..., description="Count by status")
    recent_applications: int = Field(..., description="Applications created in last 7 days")

    class Config:
        json_schema_extra = {
            "example": {
                "total": 25,
                "active": 15,
                "by_status": {
                    "draft": 3,
                    "submitted": 8,
                    "interview": 4,
                    "offer": 2,
                    "rejected": 6,
                    "accepted": 2,
                },
                "recent_applications": 5,
            }
        }
