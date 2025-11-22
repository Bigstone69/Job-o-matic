"""
Application service for managing job applications.

This service handles CRUD operations, status tracking, and history management
for job applications.
"""

from typing import List, Dict, Optional, Any
from datetime import datetime, timezone
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func, and_, or_, desc
from sqlalchemy.orm import selectinload
import logging

from src.models.database import (
    Application,
    Job,
    Company,
    ApplicationStatusHistory,
    ActivityLog,
    ApplicationStatus,
)

logger = logging.getLogger(__name__)


# Valid status transitions mapping
VALID_STATUS_TRANSITIONS: Dict[ApplicationStatus, List[ApplicationStatus]] = {
    ApplicationStatus.DRAFT: [
        ApplicationStatus.SUBMITTED,
        ApplicationStatus.WITHDRAWN,
    ],
    ApplicationStatus.SUBMITTED: [
        ApplicationStatus.SCREENING,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    ],
    ApplicationStatus.SCREENING: [
        ApplicationStatus.INTERVIEW,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    ],
    ApplicationStatus.INTERVIEW: [
        ApplicationStatus.TECHNICAL,
        ApplicationStatus.OFFER,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    ],
    ApplicationStatus.TECHNICAL: [
        ApplicationStatus.INTERVIEW,  # Can go back for more interviews
        ApplicationStatus.OFFER,
        ApplicationStatus.REJECTED,
        ApplicationStatus.WITHDRAWN,
    ],
    ApplicationStatus.OFFER: [
        ApplicationStatus.ACCEPTED,
        ApplicationStatus.REJECTED,
    ],
    ApplicationStatus.ACCEPTED: [],  # Terminal state
    ApplicationStatus.REJECTED: [],  # Terminal state
    ApplicationStatus.WITHDRAWN: [],  # Terminal state
}


class ApplicationService:
    """
    Service for managing job applications.

    Handles CRUD operations, status tracking, history, and activity logging.
    """

    def __init__(self):
        """Initialize the application service."""
        logger.info("ApplicationService initialized")

    async def create_application(
        self,
        db: AsyncSession,
        job_id: int,
        user_id: int,
        status: ApplicationStatus = ApplicationStatus.DRAFT,
        notes: Optional[str] = None,
        resume_version: Optional[str] = None,
        cover_letter_id: Optional[int] = None,
        **kwargs,
    ) -> Application:
        """
        Create a new job application.

        Args:
            db: Database session
            job_id: ID of the job being applied to
            user_id: ID of the user creating the application
            status: Initial application status (default: DRAFT)
            notes: Optional notes about the application
            resume_version: Version/name of resume used
            cover_letter_id: ID of associated cover letter
            **kwargs: Additional application fields

        Returns:
            Created Application object

        Raises:
            ValueError: If job doesn't exist
        """
        try:
            # Verify job exists
            result = await db.execute(
                select(Job).options(selectinload(Job.company)).where(Job.id == job_id)
            )
            job = result.scalar_one_or_none()

            if not job:
                raise ValueError(f"Job with ID {job_id} not found")

            # Create application
            application = Application(
                job_id=job_id,
                user_id=user_id,
                status=status,
                notes=notes,
                resume_version=resume_version,
                cover_letter_id=cover_letter_id,
                applied_date=kwargs.get("applied_date"),
                interview_date=kwargs.get("interview_date"),
                offer_deadline=kwargs.get("offer_deadline"),
                salary_offered=kwargs.get("salary_offered"),
                is_active=True,
                created_at=datetime.now(timezone.utc),
                updated_at=datetime.now(timezone.utc),
            )

            db.add(application)
            await db.flush()
            await db.refresh(application)

            # Set applied_date if submitted
            if status == ApplicationStatus.SUBMITTED and not application.applied_date:
                application.applied_date = datetime.now(timezone.utc)

            # Create initial status history
            await self._create_status_history(
                db=db,
                application_id=application.id,
                old_status=None,
                new_status=status,
                notes=f"Application created with status: {status.value}",
            )

            # Log activity
            await self._log_activity(
                db=db,
                user_id=user_id,
                action="application_created",
                entity_type="application",
                entity_id=application.id,
                metadata={
                    "job_id": job_id,
                    "job_title": job.title,
                    "company": job.company.name if job.company else None,
                    "status": status.value,
                },
            )

            logger.info(
                f"Created application {application.id} for job {job_id} by user {user_id}"
            )
            return application

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error creating application: {e}")
            raise

    async def get_application(
        self,
        db: AsyncSession,
        application_id: int,
        user_id: Optional[int] = None,
    ) -> Optional[Application]:
        """
        Get a single application by ID.

        Args:
            db: Database session
            application_id: ID of the application
            user_id: Optional user ID for ownership check

        Returns:
            Application object or None if not found
        """
        try:
            query = (
                select(Application)
                .options(
                    selectinload(Application.job).selectinload(Job.company),
                    selectinload(Application.user),
                    selectinload(Application.status_history),
                )
                .where(Application.id == application_id)
            )

            # Filter by user if specified
            if user_id is not None:
                query = query.where(Application.user_id == user_id)

            result = await db.execute(query)
            application = result.scalar_one_or_none()

            return application

        except Exception as e:
            logger.error(f"Error getting application {application_id}: {e}")
            raise

    async def get_applications(
        self,
        db: AsyncSession,
        user_id: int,
        status: Optional[ApplicationStatus] = None,
        company_id: Optional[int] = None,
        is_active: bool = True,
        skip: int = 0,
        limit: int = 100,
    ) -> List[Application]:
        """
        Get list of applications with filters.

        Args:
            db: Database session
            user_id: User ID to filter by
            status: Optional status filter
            company_id: Optional company filter
            is_active: Filter by active status (default: True)
            skip: Number of records to skip (pagination)
            limit: Maximum number of records to return

        Returns:
            List of Application objects
        """
        try:
            query = (
                select(Application)
                .options(
                    selectinload(Application.job).selectinload(Job.company),
                )
                .where(Application.user_id == user_id)
                .where(Application.is_active == is_active)
            )

            # Apply filters
            if status is not None:
                query = query.where(Application.status == status)

            if company_id is not None:
                query = query.join(Job).where(Job.company_id == company_id)

            # Order by most recent first
            query = query.order_by(desc(Application.updated_at))

            # Pagination
            query = query.offset(skip).limit(limit)

            result = await db.execute(query)
            applications = result.scalars().all()

            logger.debug(f"Retrieved {len(applications)} applications for user {user_id}")
            return list(applications)

        except Exception as e:
            logger.error(f"Error getting applications: {e}")
            raise

    async def update_application(
        self,
        db: AsyncSession,
        application_id: int,
        user_id: int,
        **updates,
    ) -> Application:
        """
        Update application fields.

        Args:
            db: Database session
            application_id: ID of the application to update
            user_id: User ID for ownership check
            **updates: Fields to update

        Returns:
            Updated Application object

        Raises:
            ValueError: If application not found or not owned by user
        """
        try:
            # Get application
            application = await self.get_application(db, application_id, user_id)
            if not application:
                raise ValueError(
                    f"Application {application_id} not found or not owned by user"
                )

            # Update allowed fields
            allowed_fields = {
                "notes",
                "resume_version",
                "cover_letter_id",
                "applied_date",
                "interview_date",
                "offer_deadline",
                "salary_offered",
            }

            updated_fields = []
            for key, value in updates.items():
                if key in allowed_fields and value is not None:
                    setattr(application, key, value)
                    updated_fields.append(key)

            if updated_fields:
                application.updated_at = datetime.now(timezone.utc)

                # Log activity
                await self._log_activity(
                    db=db,
                    user_id=user_id,
                    action="application_updated",
                    entity_type="application",
                    entity_id=application_id,
                    metadata={
                        "updated_fields": updated_fields,
                    },
                )

                logger.info(
                    f"Updated application {application_id}: {', '.join(updated_fields)}"
                )

            return application

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error updating application {application_id}: {e}")
            raise

    async def update_status(
        self,
        db: AsyncSession,
        application_id: int,
        user_id: int,
        new_status: ApplicationStatus,
        notes: Optional[str] = None,
    ) -> Application:
        """
        Update application status with validation and history tracking.

        Args:
            db: Database session
            application_id: ID of the application
            user_id: User ID for ownership check
            new_status: New status to set
            notes: Optional notes about the status change

        Returns:
            Updated Application object

        Raises:
            ValueError: If transition is invalid or application not found
        """
        try:
            # Get application
            application = await self.get_application(db, application_id, user_id)
            if not application:
                raise ValueError(
                    f"Application {application_id} not found or not owned by user"
                )

            old_status = application.status

            # Validate status transition
            if not self._is_valid_transition(old_status, new_status):
                valid_transitions = VALID_STATUS_TRANSITIONS.get(old_status, [])
                raise ValueError(
                    f"Invalid status transition from {old_status.value} to {new_status.value}. "
                    f"Valid transitions: {[s.value for s in valid_transitions]}"
                )

            # Update status
            application.status = new_status
            application.updated_at = datetime.now(timezone.utc)

            # Set applied_date if transitioning to SUBMITTED
            if new_status == ApplicationStatus.SUBMITTED and not application.applied_date:
                application.applied_date = datetime.now(timezone.utc)

            # Create status history
            await self._create_status_history(
                db=db,
                application_id=application_id,
                old_status=old_status,
                new_status=new_status,
                notes=notes,
            )

            # Log activity
            await self._log_activity(
                db=db,
                user_id=user_id,
                action="status_updated",
                entity_type="application",
                entity_id=application_id,
                metadata={
                    "old_status": old_status.value,
                    "new_status": new_status.value,
                    "notes": notes,
                },
            )

            logger.info(
                f"Updated application {application_id} status: {old_status.value} → {new_status.value}"
            )
            return application

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error updating application status: {e}")
            raise

    async def delete_application(
        self,
        db: AsyncSession,
        application_id: int,
        user_id: int,
    ) -> bool:
        """
        Soft delete an application.

        Args:
            db: Database session
            application_id: ID of the application
            user_id: User ID for ownership check

        Returns:
            True if deleted successfully

        Raises:
            ValueError: If application not found or not owned by user
        """
        try:
            # Get application
            application = await self.get_application(db, application_id, user_id)
            if not application:
                raise ValueError(
                    f"Application {application_id} not found or not owned by user"
                )

            # Soft delete
            application.is_active = False
            application.updated_at = datetime.now(timezone.utc)

            # Log activity
            await self._log_activity(
                db=db,
                user_id=user_id,
                action="application_deleted",
                entity_type="application",
                entity_id=application_id,
                metadata={
                    "status": application.status.value,
                },
            )

            logger.info(f"Deleted application {application_id}")
            return True

        except ValueError:
            raise
        except Exception as e:
            logger.error(f"Error deleting application {application_id}: {e}")
            raise

    async def get_status_history(
        self,
        db: AsyncSession,
        application_id: int,
        user_id: Optional[int] = None,
    ) -> List[ApplicationStatusHistory]:
        """
        Get status history for an application.

        Args:
            db: Database session
            application_id: ID of the application
            user_id: Optional user ID for ownership check

        Returns:
            List of ApplicationStatusHistory objects ordered by date
        """
        try:
            # Verify application exists and user owns it if user_id provided
            if user_id is not None:
                application = await self.get_application(db, application_id, user_id)
                if not application:
                    return []

            query = (
                select(ApplicationStatusHistory)
                .where(ApplicationStatusHistory.application_id == application_id)
                .order_by(desc(ApplicationStatusHistory.created_at))
            )

            result = await db.execute(query)
            history = result.scalars().all()

            return list(history)

        except Exception as e:
            logger.error(f"Error getting status history: {e}")
            raise

    async def get_application_stats(
        self,
        db: AsyncSession,
        user_id: int,
    ) -> Dict[str, Any]:
        """
        Get application statistics for a user.

        Args:
            db: Database session
            user_id: User ID

        Returns:
            Dictionary with statistics
        """
        try:
            # Count by status
            result = await db.execute(
                select(Application.status, func.count(Application.id))
                .where(Application.user_id == user_id)
                .where(Application.is_active == True)
                .group_by(Application.status)
            )
            status_counts = {status.value: count for status, count in result.all()}

            # Total applications
            total = sum(status_counts.values())

            # Active applications (not in terminal states)
            terminal_states = {
                ApplicationStatus.ACCEPTED.value,
                ApplicationStatus.REJECTED.value,
                ApplicationStatus.WITHDRAWN.value,
            }
            active = sum(
                count
                for status, count in status_counts.items()
                if status not in terminal_states
            )

            # Get recent activity count (last 7 days)
            from datetime import timedelta

            seven_days_ago = datetime.now(timezone.utc) - timedelta(days=7)
            result = await db.execute(
                select(func.count(Application.id))
                .where(Application.user_id == user_id)
                .where(Application.is_active == True)
                .where(Application.created_at >= seven_days_ago)
            )
            recent_count = result.scalar()

            return {
                "total": total,
                "active": active,
                "by_status": status_counts,
                "recent_applications": recent_count,
            }

        except Exception as e:
            logger.error(f"Error getting application stats: {e}")
            raise

    # Private helper methods

    def _is_valid_transition(
        self,
        old_status: ApplicationStatus,
        new_status: ApplicationStatus,
    ) -> bool:
        """
        Check if a status transition is valid.

        Args:
            old_status: Current status
            new_status: Desired new status

        Returns:
            True if transition is valid
        """
        # Allow staying in same status
        if old_status == new_status:
            return True

        valid_transitions = VALID_STATUS_TRANSITIONS.get(old_status, [])
        return new_status in valid_transitions

    async def _create_status_history(
        self,
        db: AsyncSession,
        application_id: int,
        old_status: Optional[ApplicationStatus],
        new_status: ApplicationStatus,
        notes: Optional[str] = None,
    ) -> ApplicationStatusHistory:
        """
        Create a status history entry.

        Args:
            db: Database session
            application_id: ID of the application
            old_status: Previous status (None for initial creation)
            new_status: New status
            notes: Optional notes about the change

        Returns:
            Created ApplicationStatusHistory object
        """
        history = ApplicationStatusHistory(
            application_id=application_id,
            old_status=old_status,
            new_status=new_status,
            notes=notes,
            created_at=datetime.now(timezone.utc),
        )

        db.add(history)
        await db.flush()

        return history

    async def _log_activity(
        self,
        db: AsyncSession,
        user_id: int,
        action: str,
        entity_type: str,
        entity_id: int,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> ActivityLog:
        """
        Log an activity.

        Args:
            db: Database session
            user_id: User performing the action
            action: Action performed
            entity_type: Type of entity (application, job, etc.)
            entity_id: ID of the entity
            metadata: Optional metadata dictionary

        Returns:
            Created ActivityLog object
        """
        activity = ActivityLog(
            user_id=user_id,
            action=action,
            entity_type=entity_type,
            entity_id=entity_id,
            metadata=metadata,
            created_at=datetime.now(timezone.utc),
        )

        db.add(activity)
        await db.flush()

        return activity
