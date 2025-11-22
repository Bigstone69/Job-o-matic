"""
Pydantic schemas for application-related API endpoints.

These schemas define request and response models for application tracking and management.
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime
from enum import Enum

from src.api.schemas.job_schemas import JobResponse


class ApplicationStatusEnum(str, Enum):
    """Application status options."""

    DRAFT = "draft"
    SUBMITTED = "submitted"
    SCREENING = "screening"
    INTERVIEW = "interview"
    TECHNICAL = "technical"
    OFFER = "offer"
    ACCEPTED = "accepted"
    REJECTED = "rejected"
    WITHDRAWN = "withdrawn"


# Request Schemas


class CreateApplicationRequest(BaseModel):
    """Request model for creating an application."""

    job_id: int = Field(..., gt=0, description="ID of the job being applied to")
    status: ApplicationStatusEnum = Field(
        default=ApplicationStatusEnum.DRAFT,
        description="Initial application status",
    )
    notes: Optional[str] = Field(None, max_length=2000, description="Application notes")
    resume_version: Optional[str] = Field(
        None, max_length=255, description="Resume version used"
    )
    cover_letter_id: Optional[int] = Field(
        None, description="ID of associated cover letter"
    )
    applied_date: Optional[datetime] = Field(None, description="Date applied")
    interview_date: Optional[datetime] = Field(None, description="Interview date")
    offer_deadline: Optional[datetime] = Field(None, description="Offer deadline date")
    salary_offered: Optional[int] = Field(None, ge=0, description="Salary offered")

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

    notes: Optional[str] = Field(None, max_length=2000)
    resume_version: Optional[str] = Field(None, max_length=255)
    cover_letter_id: Optional[int] = None
    applied_date: Optional[datetime] = None
    interview_date: Optional[datetime] = None
    offer_deadline: Optional[datetime] = None
    salary_offered: Optional[int] = Field(None, ge=0)

    class Config:
        json_schema_extra = {
            "example": {
                "notes": "Updated notes after phone screening",
                "interview_date": "2025-12-01T14:00:00Z",
            }
        }


class UpdateStatusRequest(BaseModel):
    """Request model for updating application status."""

    status: ApplicationStatusEnum = Field(..., description="New application status")
    notes: Optional[str] = Field(
        None, max_length=500, description="Notes about the status change"
    )

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
    old_status: Optional[ApplicationStatusEnum] = None
    new_status: ApplicationStatusEnum
    notes: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class ApplicationResponse(BaseModel):
    """Response model for application listing."""

    id: int
    job: JobResponse
    status: ApplicationStatusEnum
    applied_date: Optional[datetime] = None
    interview_date: Optional[datetime] = None
    offer_deadline: Optional[datetime] = None
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class ApplicationDetailResponse(ApplicationResponse):
    """Detailed response model for single application."""

    notes: Optional[str] = None
    resume_version: Optional[str] = None
    cover_letter_id: Optional[int] = None
    salary_offered: Optional[int] = None
    status_history: List[StatusHistoryResponse] = []

    class Config:
        from_attributes = True


class ApplicationStatsResponse(BaseModel):
    """Response model for application statistics."""

    total: int = Field(..., description="Total number of applications")
    active: int = Field(..., description="Active applications (non-terminal states)")
    by_status: Dict[str, int] = Field(..., description="Count by status")
    recent_applications: int = Field(
        ..., description="Applications created in last 7 days"
    )

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
