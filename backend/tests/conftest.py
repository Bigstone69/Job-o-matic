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
    Application,
    ApplicationStatusHistory,
    ActivityLog,
)
from datetime import UTC, datetime
from sqlalchemy import Table, Column, Integer, String, DateTime, MetaData


# Test database URL (use temporary file-based SQLite for tests)
# File-based ensures all connections see the same data
TEST_DATABASE_URL = "sqlite+aiosqlite:///./test_db.sqlite"

# Custom table definitions for SQLite (avoiding ARRAY type issues)
# We create simplified versions of tables that use ARRAY in PostgreSQL
test_metadata = MetaData()

users_table = Table(
    'users',
    test_metadata,
    Column('id', Integer, primary_key=True),
    Column('email', String(255), nullable=False),
    Column('username', String(100), nullable=False),
    Column('created_at', DateTime, nullable=False),
)

# Import needed types for custom table definitions
from sqlalchemy import Boolean, Text, ForeignKey, Float

# Custom companies table (simpl SQLite version)
companies_table = Table(
    'companies',
    test_metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255), nullable=False),
    Column('domain', String(255), nullable=True),
    Column('description', Text, nullable=True),
    Column('industry', String(100), nullable=True),
    Column('size', String(50), nullable=True),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
)

# Custom jobs table without ARRAY for benefits (SQLite compatible)
jobs_table = Table(
    'jobs',
    test_metadata,
    Column('id', Integer, primary_key=True),
    Column('company_id', Integer, ForeignKey('companies.id'), nullable=False),
    Column('title', String(255), nullable=False),
    Column('description', Text, nullable=True),
    Column('location', String(255), nullable=True),
    Column('job_type', String(50), nullable=True),
    Column('experience_level', String(50), nullable=True),
    Column('salary_min', Float, nullable=True),
    Column('salary_max', Float, nullable=True),
    Column('is_remote', Boolean, nullable=False, default=False),
    Column('source', String(50), nullable=False),
    Column('source_url', String(500), nullable=True),
    Column('posted_date', DateTime, nullable=True),
    Column('is_active', Boolean, nullable=False, default=True),
    Column('created_at', DateTime, nullable=False),
    Column('updated_at', DateTime, nullable=False),
    # Note: benefits field (ARRAY type in PostgreSQL) is omitted for SQLite tests
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
        # Create all custom tables (users, companies, jobs) and model tables (applications, history, activity)
        await conn.run_sync(test_metadata.create_all)
        # Create remaining model tables
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
async def test_company(db_session: AsyncSession):
    """Create a test company."""
    from sqlalchemy import insert

    # Insert company manually using custom table
    result = await db_session.execute(
        insert(companies_table).values(
            id=1,
            name="Test Company",
            domain="testcompany.com",
            description="A test company",
            industry="Technology",
            size="100-500",
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        ).returning(companies_table)
    )
    await db_session.commit()
    company_row = result.fetchone()

    # Return a simple namespace with company data
    class TestCompany:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    return TestCompany(
        id=company_row[0],
        name=company_row[1],
        domain=company_row[2],
        description=company_row[3],
        industry=company_row[4],
        size=company_row[5],
        created_at=company_row[6],
        updated_at=company_row[7],
    )


@pytest_asyncio.fixture
async def test_job(db_session: AsyncSession, test_company):
    """Create a test job."""
    from sqlalchemy import insert

    # Insert job manually using custom table (avoids ARRAY issues)
    result = await db_session.execute(
        insert(jobs_table).values(
            id=1,
            company_id=test_company.id,
            title="Software Engineer",
            description="Test job description",
            location="San Francisco, CA",
            job_type="full_time",
            experience_level="mid",
            salary_min=100000.0,
            salary_max=150000.0,
            is_remote=False,
            source="manual",
            source_url=None,
            posted_date=None,
            is_active=True,
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        ).returning(jobs_table)
    )
    await db_session.commit()
    job_row = result.fetchone()

    # Return a simple namespace with job data
    class TestJob:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)
            # Add company relationship for compatibility
            self.company = test_company

    return TestJob(
        id=job_row[0],
        company_id=job_row[1],
        title=job_row[2],
        description=job_row[3],
        location=job_row[4],
        job_type=job_row[5],
        experience_level=job_row[6],
        salary_min=job_row[7],
        salary_max=job_row[8],
        is_remote=job_row[9],
        source=job_row[10],
        source_url=job_row[11],
        posted_date=job_row[12],
        is_active=job_row[13],
        created_at=job_row[14],
        updated_at=job_row[15],
    )


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
        created_at=datetime.now(UTC),
        updated_at=datetime.now(UTC),
    )
    db_session.add(application)
    await db_session.commit()
    await db_session.refresh(application)
    return application
