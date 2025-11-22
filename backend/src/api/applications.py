"""
Application tracking and management API endpoints.

This module provides REST API endpoints for managing job applications,
tracking status changes, and viewing application history.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
import logging

from src.models.session import get_db
from src.services.application_service import ApplicationService
from src.api.schemas.application_schemas import (
    CreateApplicationRequest,
    UpdateApplicationRequest,
    UpdateStatusRequest,
    ApplicationResponse,
    ApplicationDetailResponse,
    StatusHistoryResponse,
    ApplicationStatsResponse,
    ApplicationStatusEnum,
)
from src.api.schemas.job_schemas import JobResponse, CompanyResponse

logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="/applications", tags=["applications"])

# Service instance
application_service = ApplicationService()


# Helper function to convert Application to response
def _application_to_response(app) -> ApplicationResponse:
    """Convert Application model to ApplicationResponse schema."""
    if not app.job:
        raise ValueError(f"Application {app.id} has no associated job")
    if not app.job.company:
        raise ValueError(f"Job {app.job.id} has no associated company")

    return ApplicationResponse(
        id=app.id,
        job=JobResponse(
            id=app.job.id,
            title=app.job.title,
            company=CompanyResponse(
                id=app.job.company.id,
                name=app.job.company.name,
                website=app.job.company.website,
                logo_url=app.job.company.logo_url,
                industry=app.job.company.industry,
                location=app.job.company.location,
            ),
            location=app.job.location,
            remote_policy=app.job.remote_policy,
            salary_min=app.job.salary_min,
            salary_max=app.job.salary_max,
            salary_currency=app.job.salary_currency,
            employment_type=app.job.employment_type,
            source=app.job.source,
            url=app.job.url,
            posted_date=app.job.posted_date,
            is_active=app.job.is_active,
            created_at=app.job.created_at,
        ),
        status=app.status,
        applied_date=app.applied_date,
        interview_date=app.interview_date,
        offer_deadline=app.offer_deadline,
        is_active=app.is_active,
        created_at=app.created_at,
        updated_at=app.updated_at,
    )


def _application_to_detail_response(app) -> ApplicationDetailResponse:
    """Convert Application model to ApplicationDetailResponse schema."""
    base_response = _application_to_response(app)

    # Convert status history
    history = []
    if hasattr(app, "status_history") and app.status_history:
        history = [
            StatusHistoryResponse(
                id=h.id,
                old_status=h.old_status,
                new_status=h.new_status,
                notes=h.notes,
                created_at=h.created_at,
            )
            for h in app.status_history
        ]

    return ApplicationDetailResponse(
        **base_response.model_dump(),
        notes=app.notes,
        resume_version=app.resume_version,
        cover_letter_id=app.cover_letter_id,
        salary_offered=app.salary_offered,
        status_history=history,
    )


@router.post("", response_model=ApplicationDetailResponse, status_code=201)
async def create_application(
    request: CreateApplicationRequest,
    db: AsyncSession = Depends(get_db),
) -> ApplicationDetailResponse:
    """
    Create a new job application.

    Creates a new application for a specific job, tracking the initial status
    and any associated notes or documents.
    """
    logger.info(f"Creating application for job {request.job_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        application = await application_service.create_application(
            db=db,
            job_id=request.job_id,
            user_id=user_id,
            status=request.status,
            notes=request.notes,
            resume_version=request.resume_version,
            cover_letter_id=request.cover_letter_id,
            applied_date=request.applied_date,
            interview_date=request.interview_date,
            offer_deadline=request.offer_deadline,
            salary_offered=request.salary_offered,
        )

        await db.flush()
        await db.refresh(application)

        return _application_to_detail_response(application)

    except ValueError as e:
        logger.error(f"Validation error creating application: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to create application: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create application: {str(e)}")


@router.get("", response_model=List[ApplicationResponse])
async def list_applications(
    status: Optional[ApplicationStatusEnum] = Query(None, description="Filter by status"),
    company_id: Optional[int] = Query(None, description="Filter by company ID"),
    is_active: bool = Query(True, description="Filter by active status"),
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(20, ge=1, le=100, description="Number of records to return"),
    db: AsyncSession = Depends(get_db),
) -> List[ApplicationResponse]:
    """
    List all applications for the current user.

    Supports filtering by status, company, and pagination.
    """
    logger.info(f"Listing applications: status={status}, company_id={company_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        applications = await application_service.get_applications(
            db=db,
            user_id=user_id,
            status=status,
            company_id=company_id,
            is_active=is_active,
            skip=skip,
            limit=limit,
        )

        return [_application_to_response(app) for app in applications]

    except Exception as e:
        logger.error(f"Failed to list applications: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to list applications: {str(e)}")


@router.get("/stats", response_model=ApplicationStatsResponse)
async def get_application_stats(
    db: AsyncSession = Depends(get_db),
) -> ApplicationStatsResponse:
    """
    Get application statistics for the current user.

    Returns counts by status and other useful metrics.
    """
    logger.info("Getting application statistics")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        stats = await application_service.get_application_stats(
            db=db,
            user_id=user_id,
        )

        return ApplicationStatsResponse(**stats)

    except Exception as e:
        logger.error(f"Failed to get application stats: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get stats: {str(e)}")


@router.get("/{application_id}", response_model=ApplicationDetailResponse)
async def get_application(
    application_id: int,
    db: AsyncSession = Depends(get_db),
) -> ApplicationDetailResponse:
    """
    Get detailed information about a specific application.

    Includes full job details, status history, and all application metadata.
    """
    logger.info(f"Getting application {application_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        application = await application_service.get_application(
            db=db,
            application_id=application_id,
            user_id=user_id,
        )

        if not application:
            raise HTTPException(
                status_code=404,
                detail=f"Application {application_id} not found"
            )

        return _application_to_detail_response(application)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to get application {application_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get application: {str(e)}")


@router.put("/{application_id}", response_model=ApplicationDetailResponse)
async def update_application(
    application_id: int,
    request: UpdateApplicationRequest,
    db: AsyncSession = Depends(get_db),
) -> ApplicationDetailResponse:
    """
    Update application details.

    Updates notes, dates, and other application metadata.
    Does NOT update status - use PATCH /applications/{id}/status for that.
    """
    logger.info(f"Updating application {application_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        # Convert request to dict and filter None values
        updates = {k: v for k, v in request.model_dump().items() if v is not None}

        application = await application_service.update_application(
            db=db,
            application_id=application_id,
            user_id=user_id,
            **updates,
        )

        await db.flush()
        await db.refresh(application)

        return _application_to_detail_response(application)

    except ValueError as e:
        logger.error(f"Validation error updating application: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to update application {application_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update application: {str(e)}")


@router.patch("/{application_id}/status", response_model=ApplicationDetailResponse)
async def update_application_status(
    application_id: int,
    request: UpdateStatusRequest,
    db: AsyncSession = Depends(get_db),
) -> ApplicationDetailResponse:
    """
    Update application status.

    Changes the application status with validation and history tracking.
    Invalid status transitions will be rejected.
    """
    logger.info(f"Updating status for application {application_id} to {request.status}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        application = await application_service.update_status(
            db=db,
            application_id=application_id,
            user_id=user_id,
            new_status=request.status,
            notes=request.notes,
        )

        await db.flush()
        await db.refresh(application)

        return _application_to_detail_response(application)

    except ValueError as e:
        logger.error(f"Validation error updating status: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to update application status: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to update status: {str(e)}")


@router.delete("/{application_id}", status_code=204)
async def delete_application(
    application_id: int,
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Delete an application.

    Soft delete by setting is_active to False.
    The application data is retained for historical purposes.
    """
    logger.info(f"Deleting application {application_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        await application_service.delete_application(
            db=db,
            application_id=application_id,
            user_id=user_id,
        )

        # Let dependency handle commit

    except ValueError as e:
        logger.error(f"Validation error deleting application: {e}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Failed to delete application {application_id}: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to delete application: {str(e)}")


@router.get("/{application_id}/history", response_model=List[StatusHistoryResponse])
async def get_application_history(
    application_id: int,
    db: AsyncSession = Depends(get_db),
) -> List[StatusHistoryResponse]:
    """
    Get status change history for an application.

    Returns all status changes in reverse chronological order.
    """
    logger.info(f"Getting history for application {application_id}")

    try:
        # TODO: Replace with actual user from auth
        user_id = 1

        history = await application_service.get_status_history(
            db=db,
            application_id=application_id,
            user_id=user_id,
        )

        return [
            StatusHistoryResponse(
                id=h.id,
                old_status=h.old_status,
                new_status=h.new_status,
                notes=h.notes,
                created_at=h.created_at,
            )
            for h in history
        ]

    except Exception as e:
        logger.error(f"Failed to get application history: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to get history: {str(e)}")
