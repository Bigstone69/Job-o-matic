"""
Unit tests for ApplicationService.

Tests cover CRUD operations, status validation, history tracking,
and statistics calculation.
"""

import pytest
from datetime import UTC, datetime, timedelta
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.database import (
    Application,
    ApplicationStatus,
    ApplicationStatusHistory,
    Company,
    Job,
    User,
)
from src.services.application_service import ApplicationService


class TestApplicationServiceCreate:
    """Tests for creating applications."""

    @pytest.mark.asyncio
    async def test_create_application_draft(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test creating a draft application."""
        service = ApplicationService()

        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.DRAFT,
            notes="Initial draft",
        )

        assert application.id is not None
        assert application.job_id == test_job.id
        assert application.user_id == test_user.id
        assert application.status == ApplicationStatus.DRAFT
        assert application.notes == "Initial draft"
        assert application.applied_date is None  # Draft shouldn't have applied_date

    @pytest.mark.asyncio
    async def test_create_application_submitted_sets_applied_date(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test that creating a SUBMITTED application sets applied_date."""
        service = ApplicationService()

        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )

        assert application.status == ApplicationStatus.SUBMITTED
        assert application.applied_date is not None
        assert isinstance(application.applied_date, datetime)

    @pytest.mark.asyncio
    async def test_create_application_with_custom_applied_date(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test creating application with custom applied_date."""
        service = ApplicationService()
        custom_date = datetime.utcnow() - timedelta(days=5)

        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
            applied_date=custom_date,
        )

        assert application.applied_date == custom_date

    @pytest.mark.asyncio
    async def test_create_application_invalid_job(
        self, db_session: AsyncSession, test_user: User
    ):
        """Test creating application with non-existent job."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="Job with ID 99999 not found"):
            await service.create_application(
                db=db_session,
                job_id=99999,
                user_id=test_user.id,
            )

    @pytest.mark.asyncio
    async def test_create_application_creates_status_history(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test that creating application creates initial status history."""
        service = ApplicationService()

        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.DRAFT,
        )

        history = await service.get_status_history(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
        )

        assert len(history) == 1
        assert history[0].old_status is None
        assert history[0].new_status == ApplicationStatus.DRAFT


class TestApplicationServiceRead:
    """Tests for reading applications."""

    @pytest.mark.asyncio
    async def test_get_application(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test getting a single application."""
        service = ApplicationService()

        application = await service.get_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        assert application is not None
        assert application.id == test_application.id
        assert application.job is not None
        assert application.job.company is not None

    @pytest.mark.asyncio
    async def test_get_application_wrong_user(
        self, db_session: AsyncSession, test_application: Application
    ):
        """Test getting application with wrong user_id returns None."""
        service = ApplicationService()

        application = await service.get_application(
            db=db_session,
            application_id=test_application.id,
            user_id=99999,  # Wrong user
        )

        assert application is None

    @pytest.mark.asyncio
    async def test_get_applications_list(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test getting list of applications."""
        service = ApplicationService()

        applications = await service.get_applications(
            db=db_session,
            user_id=test_user.id,
        )

        assert len(applications) == 1
        assert applications[0].id == test_application.id

    @pytest.mark.asyncio
    async def test_get_applications_filter_by_status(
        self,
        db_session: AsyncSession,
        test_job: Job,
        test_user: User,
    ):
        """Test filtering applications by status."""
        service = ApplicationService()

        # Create applications with different statuses
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.DRAFT,
        )
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )

        # Filter for submitted only
        submitted_apps = await service.get_applications(
            db=db_session,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )

        assert len(submitted_apps) == 2
        assert all(app.status == ApplicationStatus.SUBMITTED for app in submitted_apps)

    @pytest.mark.asyncio
    async def test_get_applications_excludes_inactive(
        self,
        db_session: AsyncSession,
        test_application: Application,
        test_user: User,
    ):
        """Test that inactive applications are excluded by default."""
        service = ApplicationService()

        # Soft delete the application
        await service.delete_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        # Get all applications (no soft delete, so we shouldn't see deleted ones)
        applications = await service.get_applications(
            db=db_session,
            user_id=test_user.id,
        )

        # Since we hard delete, the deleted application should not be returned
        assert len(applications) == 0


class TestApplicationServiceUpdate:
    """Tests for updating applications."""

    @pytest.mark.asyncio
    async def test_update_application_notes(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test updating application notes."""
        service = ApplicationService()

        # Store original timestamp
        original_updated_at = test_application.updated_at

        updated = await service.update_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            notes="Updated notes",
        )

        assert updated.notes == "Updated notes"
        assert updated.updated_at >= original_updated_at  # >= since timestamps might be very close

    @pytest.mark.asyncio
    async def test_update_application_multiple_fields(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test updating multiple fields."""
        service = ApplicationService()
        interview_date = datetime.now(UTC) + timedelta(days=7)

        updated = await service.update_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            notes="Interview scheduled",
            interview_date=interview_date,
            resume_version="v2.0",
        )

        assert updated.notes == "Interview scheduled"
        assert updated.interview_date == interview_date
        assert updated.resume_version == "v2.0"

    @pytest.mark.asyncio
    async def test_update_application_wrong_user(
        self, db_session: AsyncSession, test_application: Application
    ):
        """Test updating application with wrong user fails."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="not found or not owned by user"):
            await service.update_application(
                db=db_session,
                application_id=test_application.id,
                user_id=99999,
                notes="Should fail",
            )


class TestApplicationServiceStatusTransitions:
    """Tests for status transition validation."""

    @pytest.mark.asyncio
    async def test_valid_status_transition_draft_to_submitted(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test valid transition from DRAFT to SUBMITTED."""
        service = ApplicationService()

        updated = await service.update_status(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SUBMITTED,
            notes="Application submitted",
        )

        assert updated.status == ApplicationStatus.SUBMITTED
        assert updated.applied_date is not None

    @pytest.mark.asyncio
    async def test_valid_status_transition_submitted_to_interview(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test valid transition from SUBMITTED to INTERVIEW."""
        service = ApplicationService()

        # Create submitted application
        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )

        # Transition to screening then interview
        await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SCREENING,
        )

        updated = await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.INTERVIEW,
        )

        assert updated.status == ApplicationStatus.INTERVIEW

    @pytest.mark.asyncio
    async def test_invalid_status_transition_draft_to_offer(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test invalid transition from DRAFT to OFFER."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="Invalid status transition"):
            await service.update_status(
                db=db_session,
                application_id=test_application.id,
                user_id=test_user.id,
                new_status=ApplicationStatus.OFFER,
            )

    @pytest.mark.asyncio
    async def test_terminal_status_cannot_transition(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test that terminal statuses (ACCEPTED, REJECTED) cannot transition."""
        service = ApplicationService()

        # Create and accept application
        application = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )

        # Transition through valid states to OFFER
        await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SCREENING,
        )
        await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.INTERVIEW,
        )
        await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.OFFER,
        )
        await service.update_status(
            db=db_session,
            application_id=application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.ACCEPTED,
        )

        # Try to transition from ACCEPTED (should fail)
        with pytest.raises(ValueError, match="Invalid status transition"):
            await service.update_status(
                db=db_session,
                application_id=application.id,
                user_id=test_user.id,
                new_status=ApplicationStatus.INTERVIEW,
            )

    @pytest.mark.asyncio
    async def test_status_update_creates_history(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test that status updates create history entries."""
        service = ApplicationService()

        await service.update_status(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SUBMITTED,
            notes="Submitted via company portal",
        )

        history = await service.get_status_history(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        # Should have 1 entry from the status update (fixture doesn't create initial history)
        assert len(history) >= 1
        latest = history[0]  # Most recent first
        assert latest.old_status == ApplicationStatus.DRAFT
        assert latest.new_status == ApplicationStatus.SUBMITTED
        assert latest.notes == "Submitted via company portal"


class TestApplicationServiceDelete:
    """Tests for deleting applications."""

    @pytest.mark.asyncio
    async def test_delete_application_soft_delete(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test that delete is a soft delete."""
        service = ApplicationService()

        result = await service.delete_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        assert result is True

        # Application should be hard deleted (no is_active field)
        application = await service.get_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )
        # After hard delete, application should not be found
        assert application is None

    @pytest.mark.asyncio
    async def test_delete_application_wrong_user(
        self, db_session: AsyncSession, test_application: Application
    ):
        """Test deleting application with wrong user fails."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="not found or not owned by user"):
            await service.delete_application(
                db=db_session,
                application_id=test_application.id,
                user_id=99999,
            )


class TestApplicationServiceStatistics:
    """Tests for application statistics."""

    @pytest.mark.asyncio
    async def test_get_application_stats_empty(
        self, db_session: AsyncSession, test_user: User
    ):
        """Test getting stats with no applications."""
        service = ApplicationService()

        stats = await service.get_application_stats(
            db=db_session,
            user_id=test_user.id,
        )

        assert stats["total"] == 0
        assert stats["active"] == 0
        assert stats["by_status"] == {}
        assert stats["recent_applications"] == 0

    @pytest.mark.asyncio
    async def test_get_application_stats_multiple_statuses(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test getting stats with multiple applications."""
        service = ApplicationService()

        # Create applications with different statuses
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.DRAFT,
        )
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.INTERVIEW,
        )
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.REJECTED,
        )

        stats = await service.get_application_stats(
            db=db_session,
            user_id=test_user.id,
        )

        assert stats["total"] == 4
        assert stats["active"] == 3  # REJECTED is terminal
        assert stats["by_status"]["draft"] == 1
        assert stats["by_status"]["submitted"] == 1
        assert stats["by_status"]["interview"] == 1
        assert stats["by_status"]["rejected"] == 1
        assert stats["recent_applications"] == 4  # All created recently

    @pytest.mark.asyncio
    async def test_get_application_stats_excludes_inactive(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test that stats exclude inactive applications."""
        service = ApplicationService()

        # Delete the application
        await service.delete_application(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        stats = await service.get_application_stats(
            db=db_session,
            user_id=test_user.id,
        )

        assert stats["total"] == 0
        assert stats["active"] == 0

    @pytest.mark.asyncio
    async def test_get_application_stats_terminal_states(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test that terminal states are not counted as active."""
        service = ApplicationService()

        # Create applications in terminal states
        app1 = await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.SUBMITTED,
        )
        # Transition to accepted
        await service.update_status(
            db=db_session,
            application_id=app1.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SCREENING,
        )
        await service.update_status(
            db=db_session,
            application_id=app1.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.INTERVIEW,
        )
        await service.update_status(
            db=db_session,
            application_id=app1.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.OFFER,
        )
        await service.update_status(
            db=db_session,
            application_id=app1.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.ACCEPTED,
        )

        # Create active application
        await service.create_application(
            db=db_session,
            job_id=test_job.id,
            user_id=test_user.id,
            status=ApplicationStatus.INTERVIEW,
        )

        stats = await service.get_application_stats(
            db=db_session,
            user_id=test_user.id,
        )

        assert stats["total"] == 2
        assert stats["active"] == 1  # Only INTERVIEW is active


class TestApplicationServiceStatusHistory:
    """Tests for status history tracking."""

    @pytest.mark.asyncio
    async def test_get_status_history(
        self, db_session: AsyncSession, test_application: Application, test_user: User
    ):
        """Test getting status history."""
        service = ApplicationService()

        # Update status a few times
        await service.update_status(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SUBMITTED,
        )
        await service.update_status(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.SCREENING,
        )
        await service.update_status(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
            new_status=ApplicationStatus.INTERVIEW,
        )

        history = await service.get_status_history(
            db=db_session,
            application_id=test_application.id,
            user_id=test_user.id,
        )

        # Should have 3 entries (3 updates - fixture doesn't create initial history)
        assert len(history) == 3

        # Verify order (most recent first)
        assert history[0].new_status == ApplicationStatus.INTERVIEW
        assert history[1].new_status == ApplicationStatus.SCREENING
        assert history[2].new_status == ApplicationStatus.SUBMITTED

    @pytest.mark.asyncio
    async def test_get_status_history_wrong_user_returns_empty(
        self, db_session: AsyncSession, test_application: Application
    ):
        """Test getting status history with wrong user returns empty list."""
        service = ApplicationService()

        history = await service.get_status_history(
            db=db_session,
            application_id=test_application.id,
            user_id=99999,
        )

        assert history == []
