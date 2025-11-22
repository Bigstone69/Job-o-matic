"""
Job search and management API endpoints.

This module provides REST API endpoints for searching, listing, and managing jobs.
"""

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_
from sqlalchemy.orm import selectinload
from typing import List, Optional
import logging

from src.models.session import get_db
from src.models.database import Job, Company
from src.services.job_search_service import JobSearchService
from src.api.schemas.job_schemas import (
    JobSearchRequest,
    JobSearchResponse,
    JobResponse,
    JobDetailResponse,
    CreateManualJobRequest,
    CompanyResponse,
    JobListFilters,
    EmploymentTypeEnum,
    RemotePolicyEnum,
)

logger = logging.getLogger(__name__)

# Create router
router = APIRouter(prefix="/jobs", tags=["jobs"])

# Service instance (in production, use dependency injection)
job_search_service = JobSearchService()


@router.post("/search", response_model=JobSearchResponse)
async def search_jobs(
    request: JobSearchRequest,
    db: AsyncSession = Depends(get_db),
) -> JobSearchResponse:
    """
    Search for jobs across multiple platforms.

    - **query**: Job title or keywords (e.g., "Python Developer")
    - **location**: Geographic location (e.g., "San Francisco, CA")
    - **sources**: Optional list of sources to search
    - **employment_type**: Filter by employment types
    - **remote_only**: Filter for remote positions only
    - **salary_min**: Minimum salary filter
    - **max_results**: Maximum number of results (1-100)

    Returns list of matching jobs with company information.
    """
    logger.info(f"Job search request: {request.query} in {request.location}")

    try:
        # For now, use a default user_id (will be replaced with auth)
        user_id = 1

        # Perform search
        jobs = await job_search_service.search_jobs(
            db=db,
            query=request.query,
            location=request.location,
            user_id=user_id,
            sources=request.sources,
            employment_type=request.employment_type,
            remote_only=request.remote_only,
            salary_min=request.salary_min,
        )

        # Limit results
        jobs = jobs[: request.max_results]

        # Convert to response models
        job_responses = [_job_to_response(job) for job in jobs]

        return JobSearchResponse(
            jobs=job_responses,
            total=len(job_responses),
            page=1,
            per_page=request.max_results,
            search_query=request.query,
            search_location=request.location,
        )

    except Exception as e:
        logger.error(f"Job search failed: {e}")
        raise HTTPException(status_code=500, detail=f"Job search failed: {str(e)}")


@router.get("", response_model=List[JobResponse])
async def list_jobs(
    skip: int = Query(0, ge=0, description="Number of jobs to skip"),
    limit: int = Query(20, ge=1, le=100, description="Number of jobs to return"),
    company_id: Optional[int] = Query(None, description="Filter by company ID"),
    location: Optional[str] = Query(None, description="Filter by location"),
    employment_type: Optional[EmploymentTypeEnum] = Query(
        None, description="Filter by employment type"
    ),
    remote_policy: Optional[RemotePolicyEnum] = Query(
        None, description="Filter by remote policy"
    ),
    is_active: bool = Query(True, description="Filter by active status"),
    db: AsyncSession = Depends(get_db),
) -> List[JobResponse]:
    """
    List saved jobs with optional filters.

    Supports pagination and various filters to narrow down results.
    """
    logger.info(f"Listing jobs: skip={skip}, limit={limit}")

    try:
        # Build query with filters and eager load company relationship
        query = select(Job).options(selectinload(Job.company)).where(Job.is_active == is_active)

        if company_id:
            query = query.where(Job.company_id == company_id)
        if location:
            query = query.where(Job.location.ilike(f"%{location}%"))
        if employment_type:
            query = query.where(Job.employment_type == employment_type)
        if remote_policy:
            query = query.where(Job.remote_policy == remote_policy)

        # Add pagination
        query = query.offset(skip).limit(limit)

        # Execute query
        result = await db.execute(query)
        jobs = result.scalars().all()

        # Convert to response models
        return [_job_to_response(job) for job in jobs]

    except Exception as e:
        logger.error(f"Failed to list jobs: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to list jobs: {str(e)}")


@router.get("/{job_id}", response_model=JobDetailResponse)
async def get_job(
    job_id: int,
    db: AsyncSession = Depends(get_db),
) -> JobDetailResponse:
    """
    Get detailed information about a specific job.

    Returns full job details including description and parsed requirements.
    """
    logger.info(f"Fetching job: {job_id}")

    try:
        result = await db.execute(
            select(Job).options(selectinload(Job.company)).where(Job.id == job_id)
        )
        job = result.scalar_one_or_none()

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

        return _job_to_detail_response(job)

    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Failed to fetch job: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch job: {str(e)}")


@router.post("", response_model=JobDetailResponse, status_code=201)
async def create_manual_job(
    request: CreateManualJobRequest,
    db: AsyncSession = Depends(get_db),
) -> JobDetailResponse:
    """
    Manually create a job entry.

    Use this endpoint to add jobs found outside of automated searches,
    such as through networking or direct company websites.
    """
    logger.info(f"Creating manual job: {request.title} at {request.company_name}")

    try:
        job = await job_search_service.create_manual_job(
            db=db,
            title=request.title,
            company_name=request.company_name,
            url=request.url,
            location=request.location,
            description=request.description,
            employment_type=request.employment_type.value,
            remote_policy=request.remote_policy.value,
            salary_min=request.salary_min,
            salary_max=request.salary_max,
            salary_currency=request.salary_currency,
            posted_date=request.posted_date,
        )

        await db.commit()
        await db.refresh(job)

        return _job_to_detail_response(job)

    except Exception as e:
        await db.rollback()
        logger.error(f"Failed to create manual job: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to create job: {str(e)}")


@router.delete("/{job_id}", status_code=204)
async def delete_job(
    job_id: int,
    db: AsyncSession = Depends(get_db),
) -> None:
    """
    Delete a job entry.

    Soft delete by setting is_active to False.
    """
    logger.info(f"Deleting job: {job_id}")

    try:
        result = await db.execute(
            select(Job).options(selectinload(Job.company)).where(Job.id == job_id)
        )
        job = result.scalar_one_or_none()

        if not job:
            raise HTTPException(status_code=404, detail=f"Job {job_id} not found")

        job.is_active = False
        await db.commit()

    except HTTPException:
        raise
    except Exception as e:
        await db.rollback()
        logger.error(f"Failed to delete job: {e}")
        raise HTTPException(status_code=500, detail=f"Failed to delete job: {str(e)}")


# Helper functions


def _job_to_response(job: Job) -> JobResponse:
    """Convert Job model to JobResponse schema."""
    if not job.company:
        raise ValueError(f"Job {job.id} has no associated company")

    return JobResponse(
        id=job.id,
        title=job.title,
        company=CompanyResponse(
            id=job.company.id,
            name=job.company.name,
            website=job.company.website,
            logo_url=job.company.logo_url,
            industry=job.company.industry,
            location=job.company.location,
        ),
        location=job.location,
        remote_policy=job.remote_policy,
        salary_min=job.salary_min,
        salary_max=job.salary_max,
        salary_currency=job.salary_currency,
        employment_type=job.employment_type,
        source=job.source,
        url=job.url,
        posted_date=job.posted_date,
        is_active=job.is_active,
        created_at=job.created_at,
    )


def _job_to_detail_response(job: Job) -> JobDetailResponse:
    """Convert Job model to JobDetailResponse schema."""
    if not job.company:
        raise ValueError(f"Job {job.id} has no associated company")

    return JobDetailResponse(
        id=job.id,
        title=job.title,
        company=CompanyResponse(
            id=job.company.id,
            name=job.company.name,
            website=job.company.website,
            logo_url=job.company.logo_url,
            industry=job.company.industry,
            location=job.company.location,
        ),
        location=job.location,
        description=job.description,
        remote_policy=job.remote_policy,
        salary_min=job.salary_min,
        salary_max=job.salary_max,
        salary_currency=job.salary_currency,
        employment_type=job.employment_type,
        source=job.source,
        source_id=job.source_id,
        url=job.url,
        posted_date=job.posted_date,
        benefits=job.benefits,
        requirements_parsed=job.requirements_parsed,
        is_active=job.is_active,
        created_at=job.created_at,
        updated_at=job.updated_at,
    )
