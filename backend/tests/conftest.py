"""
Pytest configuration and fixtures for backend tests.
"""

import asyncio
from typing import AsyncGenerator, Generator

import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import NullPool

from src.models.database import (
    Base,
    User,
    Company,
    Job,
    ApplicationStatus,
    Application,
    ApplicationStatusHistory,
    ActivityLog,
)
from datetime import UTC, datetime


# Test database URL (PostgreSQL for full compatibility)
TEST_DATABASE_URL = "postgresql+asyncpg://test_user:test_password@localhost:5432/test_jobomatic"


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="function")
async def db_engine():
    """Create a test database engine."""
    engine = create_async_engine(
        TEST_DATABASE_URL,
        poolclass=NullPool,
        echo=False,
    )

    async with engine.begin() as conn:
        # Create all tables from ORM models (PostgreSQL supports all types)
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    async with engine.begin() as conn:
        # Clean up all tables
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest_asyncio.fixture(scope="function")
async def db_session(db_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create a test database session."""
    async_session_factory = async_sessionmaker(
        db_engine,
        class_=AsyncSession,
        expire_on_commit=False,
    )

    async with async_session_factory() as session:
        yield session
        await session.rollback()


@pytest_asyncio.fixture
async def test_user(db_session: AsyncSession) -> User:
    """Create a test user."""
    user = User(
        id=1,
        email="test@example.com",
        username="testuser",
        hashed_password="test_hashed_password",
        is_active=True,
    )
    db_session.add(user)
    await db_session.commit()
    await db_session.refresh(user)
    return user


@pytest_asyncio.fixture
async def test_company(db_session: AsyncSession) -> Company:
    """Create a test company."""
    company = Company(
        id=1,
        name="Test Company",
        website="https://testcompany.com",
        description="A test company",
        industry="Technology",
        employee_count="100-500",
    )
    db_session.add(company)
    await db_session.commit()
    await db_session.refresh(company)
    return company


@pytest_asyncio.fixture
async def test_job(db_session: AsyncSession, test_company: Company) -> Job:
    """Create a test job."""
    job = Job(
        id=1,
        company_id=test_company.id,
        title="Software Engineer",
        description="Test job description",
        location="San Francisco, CA",
        employment_type="full_time",
        experience_level="mid",
        salary_min=100000.0,
        salary_max=150000.0,
        url="https://example.com/job/1",
        source="manual",
        is_active=True,
    )
    db_session.add(job)
    await db_session.commit()
    await db_session.refresh(job)
    return job


@pytest_asyncio.fixture
async def test_application(
    db_session: AsyncSession, test_job, test_user
) -> Application:
    """Create a test application."""
    application = Application(
        id=1,
        job_id=test_job.id,
        user_id=test_user.id,
        status=ApplicationStatus.DRAFT,
        notes="Test application notes",
        is_active=True,
    )
    db_session.add(application)
    await db_session.commit()
    await db_session.refresh(application)
    return application
