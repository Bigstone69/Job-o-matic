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
    ApplicationStatus,
    Company,
    Job,
    Application,
    ApplicationStatusHistory,
    ActivityLog,
)
from datetime import UTC, datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData


# Test database URL (use in-memory SQLite for fast tests)
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"

# Simple User table for SQLite (avoiding ARRAY type issues)
test_metadata = MetaData()
users_table = Table(
    'users',
    test_metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(255), nullable=False),
    Column('username', String(100), nullable=False),
    Column('created_at', DateTime, nullable=False),
)


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
        # Create only the tables we need (skip User model to avoid ARRAY issues)
        await conn.run_sync(test_metadata.create_all)
        await conn.run_sync(Company.__table__.create, checkfirst=True)
        await conn.run_sync(Job.__table__.create, checkfirst=True)
        await conn.run_sync(Application.__table__.create, checkfirst=True)
        await conn.run_sync(ApplicationStatusHistory.__table__.create, checkfirst=True)
        await conn.run_sync(ActivityLog.__table__.create, checkfirst=True)

    yield engine

    async with engine.begin() as conn:
        await conn.run_sync(test_metadata.drop_all)
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
async def test_user(db_session: AsyncSession):
    """Create a test user."""
    from sqlalchemy import insert

    # Insert user manually to avoid User model ARRAY issues
    result = await db_session.execute(
        insert(users_table).values(
            id=1,
            email="test@example.com",
            username="testuser",
            created_at=datetime.now(UTC),
        ).returning(users_table)
    )
    await db_session.commit()
    user_row = result.fetchone()

    # Return a simple namespace with user data
    class TestUser:
        def __init__(self, id, email, username, created_at):
            self.id = id
            self.email = email
            self.username = username
            self.created_at = created_at

    return TestUser(
        id=user_row[0],
        email=user_row[1],
        username=user_row[2],
        created_at=user_row[3],
    )


@pytest_asyncio.fixture
async def test_company(db_session: AsyncSession) -> Company:
    """Create a test company."""
    company = Company(
        id=1,
        name="Test Company",
        domain="testcompany.com",
        description="A test company",
        industry="Technology",
        size="100-500",
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
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
        job_type="full_time",
        experience_level="mid",
        salary_min=100000,
        salary_max=150000,
        is_remote=False,
        source="manual",
        is_active=True,
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )
    db_session.add(job)
    await db_session.commit()
    await db_session.refresh(job)
    return job


@pytest_asyncio.fixture
async def test_application(
    db_session: AsyncSession, test_job: Job, test_user
) -> Application:
    """Create a test application."""
    application = Application(
        id=1,
        job_id=test_job.id,
        user_id=test_user.id,
        status=ApplicationStatus.DRAFT,
        notes="Test application notes",
        is_active=True,
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )
    db_session.add(application)
    await db_session.commit()
    await db_session.refresh(application)
    return application
