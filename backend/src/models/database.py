"""
Database models for Job-o-matic application.

This module defines all SQLAlchemy ORM models for the job application management system,
including Jobs, Applications, Cover Letters, Users, Companies, and related entities.
"""

import enum
from datetime import datetime

from sqlalchemy import JSON, DateTime, Enum, ForeignKey, Index, Integer, String, Text
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Base class for all database models."""


class ApplicationStatus(str, enum.Enum):
    """Application status enum."""

    INTERESTED = "interested"
    APPLIED = "applied"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"


class RemotePolicy(str, enum.Enum):
    """Remote work policy enum."""

    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"
    UNKNOWN = "unknown"


class EmploymentType(str, enum.Enum):
    """Employment type enum."""

    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"


class User(Base):
    """User model for storing user profile and preferences."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    resume_text: Mapped[str | None] = mapped_column(Text, nullable=True)
    skills: Mapped[list[str]] = mapped_column(ARRAY(String), default=list, nullable=False)
    preferences: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    applications: Mapped[list["Application"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    search_queries: Mapped[list["SearchQuery"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    activity_logs: Mapped[list["ActivityLog"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self) -> str:
        return f"<User(id={self.id}, email='{self.email}', name='{self.name}')>"


class Company(Base):
    """Company model for storing employer information."""

    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    website: Mapped[str | None] = mapped_column(String(500), nullable=True)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    industry: Mapped[str | None] = mapped_column(String(100), nullable=True)
    logo_url: Mapped[str | None] = mapped_column(String(500), nullable=True)
    location: Mapped[str | None] = mapped_column(String(255), nullable=True)
    employee_count: Mapped[str | None] = mapped_column(String(50), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    jobs: Mapped[list["Job"]] = relationship(back_populates="company", cascade="all, delete-orphan")

    # Indexes
    __table_args__ = (Index("idx_company_name", "name"),)

    def __repr__(self) -> str:
        return f"<Company(id={self.id}, name='{self.name}')>"


class Job(Base):
    """Job model for storing job postings."""

    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(255), index=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    remote_policy: Mapped[RemotePolicy] = mapped_column(
        Enum(RemotePolicy), default=RemotePolicy.UNKNOWN, nullable=False
    )
    salary_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_currency: Mapped[str] = mapped_column(String(3), default="USD", nullable=False)
    employment_type: Mapped[EmploymentType] = mapped_column(Enum(EmploymentType), nullable=False)
    source: Mapped[str] = mapped_column(String(50), nullable=False)  # "jobspy", "scraped", "manual"
    source_id: Mapped[str | None] = mapped_column(
        String(255), nullable=True
    )  # External ID from source
    url: Mapped[str] = mapped_column(String(1000), nullable=False)
    posted_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)

    # Parsed requirements from LLM analysis
    requirements_parsed: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    # Structure: {
    #   "required_skills": ["Python", "FastAPI"],
    #   "preferred_skills": ["Docker", "AWS"],
    #   "experience_years": "3-5",
    #   "education": "Bachelor's in CS",
    #   "match_score": 85
    # }

    # Additional metadata
    benefits: Mapped[list[str] | None] = mapped_column(ARRAY(String), nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    company: Mapped["Company"] = relationship(back_populates="jobs")
    applications: Mapped[list["Application"]] = relationship(
        back_populates="job", cascade="all, delete-orphan"
    )

    # Indexes
    __table_args__ = (
        Index("idx_job_title", "title"),
        Index("idx_job_location", "location"),
        Index("idx_job_posted_date", "posted_date"),
        Index("idx_job_source", "source", "source_id"),
        Index("idx_job_active", "is_active"),
    )

    def __repr__(self) -> str:
        return f"<Job(id={self.id}, title='{self.title}', company_id={self.company_id})>"


class Application(Base):
    """Application model for tracking job applications."""

    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    status: Mapped[ApplicationStatus] = mapped_column(
        Enum(ApplicationStatus), default=ApplicationStatus.INTERESTED, nullable=False
    )
    applied_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    response_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    resume_version: Mapped[str | None] = mapped_column(String(100), nullable=True)
    contact_name: Mapped[str | None] = mapped_column(String(255), nullable=True)
    contact_email: Mapped[str | None] = mapped_column(String(255), nullable=True)
    referral: Mapped[str | None] = mapped_column(String(255), nullable=True)
    follow_up_date: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    job: Mapped["Job"] = relationship(back_populates="applications")
    user: Mapped["User"] = relationship(back_populates="applications")
    cover_letters: Mapped[list["CoverLetter"]] = relationship(
        back_populates="application", cascade="all, delete-orphan"
    )
    status_history: Mapped[list["ApplicationStatusHistory"]] = relationship(
        back_populates="application", cascade="all, delete-orphan"
    )

    # Indexes
    __table_args__ = (
        Index("idx_application_user", "user_id"),
        Index("idx_application_status", "status"),
        Index("idx_application_applied_date", "applied_date"),
    )

    def __repr__(self) -> str:
        return f"<Application(id={self.id}, job_id={self.job_id}, status={self.status})>"


class ApplicationStatusHistory(Base):
    """Track status changes for applications."""

    __tablename__ = "application_status_history"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), nullable=False)
    old_status: Mapped[ApplicationStatus | None] = mapped_column(
        Enum(ApplicationStatus), nullable=True
    )
    new_status: Mapped[ApplicationStatus] = mapped_column(Enum(ApplicationStatus), nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    application: Mapped["Application"] = relationship(back_populates="status_history")

    # Indexes
    __table_args__ = (Index("idx_status_history_application", "application_id"),)

    def __repr__(self) -> str:
        return f"<StatusHistory(id={self.id}, {self.old_status} → {self.new_status})>"


class CoverLetter(Base):
    """Cover letter model for storing generated cover letters."""

    __tablename__ = "cover_letters"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    version: Mapped[int] = mapped_column(Integer, default=1, nullable=False)
    llm_provider: Mapped[str] = mapped_column(String(50), nullable=False)  # "claude", "ollama"
    llm_model: Mapped[str | None] = mapped_column(String(100), nullable=True)
    style: Mapped[str] = mapped_column(
        String(50), default="professional", nullable=False
    )  # "professional", "casual", "creative"
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    # Relationships
    application: Mapped["Application"] = relationship(back_populates="cover_letters")

    # Indexes
    __table_args__ = (
        Index("idx_cover_letter_application", "application_id"),
        Index("idx_cover_letter_version", "application_id", "version"),
    )

    def __repr__(self) -> str:
        return f"<CoverLetter(id={self.id}, application_id={self.application_id}, version={self.version})>"


class SearchQuery(Base):
    """Search query model for tracking job searches."""

    __tablename__ = "search_queries"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    query: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    filters: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    # filters structure: {"remote_only": true, "salary_min": 100000, "employment_type": ["full_time"]}
    results_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    source: Mapped[str] = mapped_column(
        String(50), default="api", nullable=False
    )  # "api", "scraped"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="search_queries")

    # Indexes
    __table_args__ = (
        Index("idx_search_query_user", "user_id"),
        Index("idx_search_query_created", "created_at"),
    )

    def __repr__(self) -> str:
        return f"<SearchQuery(id={self.id}, query='{self.query}', location='{self.location}')>"


class ActivityLog(Base):
    """Activity log model for tracking user actions."""

    __tablename__ = "activity_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    action_type: Mapped[str] = mapped_column(
        String(50), nullable=False
    )  # "job_search", "application_created", "cover_letter_generated", etc.
    entity_type: Mapped[str | None] = mapped_column(
        String(50), nullable=True
    )  # "job", "application", "cover_letter"
    entity_id: Mapped[int | None] = mapped_column(Integer, nullable=True)
    details: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    user_agent: Mapped[str | None] = mapped_column(String(500), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="activity_logs")

    # Indexes
    __table_args__ = (
        Index("idx_activity_log_user", "user_id"),
        Index("idx_activity_log_action", "action_type"),
        Index("idx_activity_log_created", "created_at"),
        Index("idx_activity_log_entity", "entity_type", "entity_id"),
    )

    def __repr__(self) -> str:
        return f"<ActivityLog(id={self.id}, action='{self.action_type}', user_id={self.user_id})>"
