"""initial schema

Revision ID: 001
Revises:
Create Date: 2025-11-22 15:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create enum types
    op.execute(
        """
        CREATE TYPE applicationstatus AS ENUM (
            'interested', 'applied', 'screening', 'interview',
            'offer', 'rejected', 'accepted', 'withdrawn'
        )
    """
    )
    op.execute(
        """
        CREATE TYPE remotepolicy AS ENUM ('remote', 'hybrid', 'onsite', 'unknown')
    """
    )
    op.execute(
        """
        CREATE TYPE employmenttype AS ENUM (
            'full_time', 'part_time', 'contract', 'temporary', 'internship'
        )
    """
    )

    # Create users table
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("resume_text", sa.Text(), nullable=True),
        sa.Column(
            "skills", postgresql.ARRAY(sa.String()), nullable=False, server_default="{}"
        ),
        sa.Column("preferences", postgresql.JSON(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_email"), "users", ["email"], unique=True)

    # Create companies table
    op.create_table(
        "companies",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=255), nullable=False),
        sa.Column("website", sa.String(length=500), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("industry", sa.String(length=100), nullable=True),
        sa.Column("logo_url", sa.String(length=500), nullable=True),
        sa.Column("location", sa.String(length=255), nullable=True),
        sa.Column("employee_count", sa.String(length=50), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_company_name", "companies", ["name"])

    # Create jobs table
    op.create_table(
        "jobs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("company_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=False),
        sa.Column(
            "remote_policy",
            sa.Enum(
                "remote", "hybrid", "onsite", "unknown", name="remotepolicy"
            ),
            nullable=False,
        ),
        sa.Column("salary_min", sa.Integer(), nullable=True),
        sa.Column("salary_max", sa.Integer(), nullable=True),
        sa.Column("salary_currency", sa.String(length=3), nullable=False),
        sa.Column(
            "employment_type",
            sa.Enum(
                "full_time",
                "part_time",
                "contract",
                "temporary",
                "internship",
                name="employmenttype",
            ),
            nullable=False,
        ),
        sa.Column("source", sa.String(length=50), nullable=False),
        sa.Column("source_id", sa.String(length=255), nullable=True),
        sa.Column("url", sa.String(length=1000), nullable=False),
        sa.Column("posted_date", sa.DateTime(), nullable=True),
        sa.Column("requirements_parsed", postgresql.JSON(), nullable=True),
        sa.Column("benefits", postgresql.ARRAY(sa.String()), nullable=True),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["company_id"], ["companies.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_job_title", "jobs", ["title"])
    op.create_index("idx_job_location", "jobs", ["location"])
    op.create_index("idx_job_posted_date", "jobs", ["posted_date"])
    op.create_index("idx_job_source", "jobs", ["source", "source_id"])
    op.create_index("idx_job_active", "jobs", ["is_active"])

    # Create applications table
    op.create_table(
        "applications",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("job_id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column(
            "status",
            sa.Enum(
                "interested",
                "applied",
                "screening",
                "interview",
                "offer",
                "rejected",
                "accepted",
                "withdrawn",
                name="applicationstatus",
            ),
            nullable=False,
        ),
        sa.Column("applied_date", sa.DateTime(), nullable=True),
        sa.Column("response_date", sa.DateTime(), nullable=True),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("resume_version", sa.String(length=100), nullable=True),
        sa.Column("contact_name", sa.String(length=255), nullable=True),
        sa.Column("contact_email", sa.String(length=255), nullable=True),
        sa.Column("referral", sa.String(length=255), nullable=True),
        sa.Column("follow_up_date", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["job_id"], ["jobs.id"]),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_application_user", "applications", ["user_id"])
    op.create_index("idx_application_status", "applications", ["status"])
    op.create_index("idx_application_applied_date", "applications", ["applied_date"])

    # Create application_status_history table
    op.create_table(
        "application_status_history",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("application_id", sa.Integer(), nullable=False),
        sa.Column(
            "old_status",
            sa.Enum(
                "interested",
                "applied",
                "screening",
                "interview",
                "offer",
                "rejected",
                "accepted",
                "withdrawn",
                name="applicationstatus",
            ),
            nullable=True,
        ),
        sa.Column(
            "new_status",
            sa.Enum(
                "interested",
                "applied",
                "screening",
                "interview",
                "offer",
                "rejected",
                "accepted",
                "withdrawn",
                name="applicationstatus",
            ),
            nullable=False,
        ),
        sa.Column("notes", sa.Text(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["application_id"], ["applications.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        "idx_status_history_application", "application_status_history", ["application_id"]
    )

    # Create cover_letters table
    op.create_table(
        "cover_letters",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("application_id", sa.Integer(), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("version", sa.Integer(), nullable=False),
        sa.Column("llm_provider", sa.String(length=50), nullable=False),
        sa.Column("llm_model", sa.String(length=100), nullable=True),
        sa.Column("style", sa.String(length=50), nullable=False),
        sa.Column("is_active", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["application_id"], ["applications.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_cover_letter_application", "cover_letters", ["application_id"])
    op.create_index(
        "idx_cover_letter_version", "cover_letters", ["application_id", "version"]
    )

    # Create search_queries table
    op.create_table(
        "search_queries",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("query", sa.String(length=500), nullable=False),
        sa.Column("location", sa.String(length=255), nullable=False),
        sa.Column("filters", postgresql.JSON(), nullable=True),
        sa.Column("results_count", sa.Integer(), nullable=False),
        sa.Column("source", sa.String(length=50), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_search_query_user", "search_queries", ["user_id"])
    op.create_index("idx_search_query_created", "search_queries", ["created_at"])

    # Create activity_logs table
    op.create_table(
        "activity_logs",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("action_type", sa.String(length=50), nullable=False),
        sa.Column("entity_type", sa.String(length=50), nullable=True),
        sa.Column("entity_id", sa.Integer(), nullable=True),
        sa.Column("details", postgresql.JSON(), nullable=True),
        sa.Column("ip_address", sa.String(length=45), nullable=True),
        sa.Column("user_agent", sa.String(length=500), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"]),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("idx_activity_log_user", "activity_logs", ["user_id"])
    op.create_index("idx_activity_log_action", "activity_logs", ["action_type"])
    op.create_index("idx_activity_log_created", "activity_logs", ["created_at"])
    op.create_index(
        "idx_activity_log_entity", "activity_logs", ["entity_type", "entity_id"]
    )


def downgrade() -> None:
    # Drop tables in reverse order
    op.drop_index("idx_activity_log_entity", table_name="activity_logs")
    op.drop_index("idx_activity_log_created", table_name="activity_logs")
    op.drop_index("idx_activity_log_action", table_name="activity_logs")
    op.drop_index("idx_activity_log_user", table_name="activity_logs")
    op.drop_table("activity_logs")

    op.drop_index("idx_search_query_created", table_name="search_queries")
    op.drop_index("idx_search_query_user", table_name="search_queries")
    op.drop_table("search_queries")

    op.drop_index("idx_cover_letter_version", table_name="cover_letters")
    op.drop_index("idx_cover_letter_application", table_name="cover_letters")
    op.drop_table("cover_letters")

    op.drop_index("idx_status_history_application", table_name="application_status_history")
    op.drop_table("application_status_history")

    op.drop_index("idx_application_applied_date", table_name="applications")
    op.drop_index("idx_application_status", table_name="applications")
    op.drop_index("idx_application_user", table_name="applications")
    op.drop_table("applications")

    op.drop_index("idx_job_active", table_name="jobs")
    op.drop_index("idx_job_source", table_name="jobs")
    op.drop_index("idx_job_posted_date", table_name="jobs")
    op.drop_index("idx_job_location", table_name="jobs")
    op.drop_index("idx_job_title", table_name="jobs")
    op.drop_table("jobs")

    op.drop_index("idx_company_name", table_name="companies")
    op.drop_table("companies")

    op.drop_index(op.f("ix_users_email"), table_name="users")
    op.drop_table("users")

    # Drop enum types
    op.execute("DROP TYPE employmenttype")
    op.execute("DROP TYPE remotepolicy")
    op.execute("DROP TYPE applicationstatus")
