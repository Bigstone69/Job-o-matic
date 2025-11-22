# Backend Test Methodology

**Comprehensive Testing Guide for Job-o-matic Backend**

Version: 1.0
Date: November 22, 2025

---

## Table of Contents

1. [Testing Philosophy](#testing-philosophy)
2. [Test Structure & Organization](#test-structure--organization)
3. [Unit Testing Patterns](#unit-testing-patterns)
4. [Integration Testing Patterns](#integration-testing-patterns)
5. [Testing Best Practices](#testing-best-practices)
6. [Database Testing Strategy](#database-testing-strategy)
7. [Mocking & Fixtures](#mocking--fixtures)
8. [Coverage Targets](#coverage-targets)
9. [Implementation Examples](#implementation-examples)
10. [Common Patterns & Anti-patterns](#common-patterns--anti-patterns)

---

## Testing Philosophy

### Guiding Principles

**1. Test Behavior, Not Implementation**
- Focus on what the code does, not how it does it
- Tests should survive refactoring
- Mock external dependencies, not internal logic

**2. Tests as Documentation**
- Test names should describe the behavior being tested
- Good test names: `test_create_application_submitted_sets_applied_date`
- Bad test names: `test_create`, `test_function_1`

**3. Fast, Isolated, Repeatable**
- Unit tests should run in milliseconds
- Each test should be independent
- Tests should pass reliably (no flaky tests)

**4. Arrange-Act-Assert (AAA) Pattern**
```python
async def test_create_application():
    # Arrange: Set up test data
    user_id = 1
    job_id = 1

    # Act: Execute the behavior
    application = await service.create_application(db, job_id, user_id)

    # Assert: Verify the results
    assert application.id is not None
    assert application.user_id == user_id
    assert application.job_id == job_id
```

### Testing Pyramid

```
         /\
        /  \  E2E Tests (5%)
       /____\
      /      \  Integration Tests (15%)
     /________\
    /          \  Unit Tests (80%)
   /____________\
```

**80% Unit Tests:**
- Service layer business logic
- Utility functions
- Validators and helpers

**15% Integration Tests:**
- API endpoints
- Database operations
- External service integration

**5% E2E Tests:**
- Critical user flows
- Cross-system integration

---

## Test Structure & Organization

### Directory Structure

```
backend/
├── tests/
│   ├── conftest.py                 # Shared fixtures
│   ├── test_application_service.py # Service layer tests
│   ├── test_job_search_service.py  # Service layer tests
│   ├── test_api_applications.py    # API integration tests
│   ├── test_api_jobs.py            # API integration tests
│   ├── test_models.py              # Model tests
│   ├── test_utils.py               # Utility tests
│   └── integration/                # Integration tests
│       ├── test_database.py
│       └── test_external_apis.py
```

### Test File Naming

- **Service tests:** `test_{service_name}_service.py`
- **API tests:** `test_api_{resource}.py`
- **Model tests:** `test_models.py` or `test_{model_name}.py`
- **Utility tests:** `test_{module_name}.py`

### Test Class Organization

Group related tests into classes for better organization:

```python
class TestApplicationServiceCreate:
    """Tests for creating applications."""

    async def test_create_draft_application(self): ...
    async def test_create_submitted_application(self): ...
    async def test_create_invalid_job_raises_error(self): ...

class TestApplicationServiceRead:
    """Tests for reading applications."""

    async def test_get_application_by_id(self): ...
    async def test_list_applications(self): ...
    async def test_filter_applications_by_status(self): ...

class TestApplicationServiceUpdate:
    """Tests for updating applications."""

    async def test_update_application_notes(self): ...
    async def test_update_application_status(self): ...
```

---

## Unit Testing Patterns

### Service Layer Testing

**Goal:** Test business logic in isolation

**Pattern:**
```python
@pytest.mark.asyncio
async def test_service_method(db_session: AsyncSession, test_fixtures):
    # Arrange
    service = ServiceClass()
    test_data = {...}

    # Act
    result = await service.method(db_session, test_data)

    # Assert
    assert result.property == expected_value
```

**Example: Testing ApplicationService**

```python
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
        assert application.status == ApplicationStatus.DRAFT
        assert application.applied_date is None  # Draft shouldn't set date
        assert application.is_active is True
        assert application.notes == "Initial draft"

    @pytest.mark.asyncio
    async def test_create_application_submitted_sets_applied_date(
        self, db_session: AsyncSession, test_job: Job, test_user: User
    ):
        """Test that SUBMITTED status auto-sets applied_date."""
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
    async def test_create_application_invalid_job_raises_error(
        self, db_session: AsyncSession, test_user: User
    ):
        """Test that invalid job ID raises ValueError."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="Job .* not found"):
            await service.create_application(
                db=db_session,
                job_id=99999,  # Non-existent job
                user_id=test_user.id,
                status=ApplicationStatus.DRAFT,
            )
```

### Testing Status Transitions

```python
class TestApplicationServiceStatusTransitions:
    """Tests for status transition validation."""

    @pytest.mark.asyncio
    async def test_valid_transition_draft_to_submitted(
        self, db_session: AsyncSession, test_application_draft
    ):
        """Test valid transition: DRAFT -> SUBMITTED."""
        service = ApplicationService()

        result = await service.update_status(
            db=db_session,
            application_id=test_application_draft.id,
            user_id=test_application_draft.user_id,
            new_status=ApplicationStatus.SUBMITTED,
            notes="Submitted application",
        )

        assert result.status == ApplicationStatus.SUBMITTED
        assert result.applied_date is not None

    @pytest.mark.asyncio
    async def test_invalid_transition_draft_to_offer_raises_error(
        self, db_session: AsyncSession, test_application_draft
    ):
        """Test invalid transition: DRAFT -> OFFER (should fail)."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="Invalid status transition"):
            await service.update_status(
                db=db_session,
                application_id=test_application_draft.id,
                user_id=test_application_draft.user_id,
                new_status=ApplicationStatus.OFFER,
                notes="Invalid transition",
            )

    @pytest.mark.asyncio
    async def test_terminal_status_cannot_transition(
        self, db_session: AsyncSession, test_application_accepted
    ):
        """Test that terminal statuses (ACCEPTED) cannot transition."""
        service = ApplicationService()

        with pytest.raises(ValueError, match="Cannot transition from terminal status"):
            await service.update_status(
                db=db_session,
                application_id=test_application_accepted.id,
                user_id=test_application_accepted.user_id,
                new_status=ApplicationStatus.INTERVIEW,
            )
```

---

## Integration Testing Patterns

### API Endpoint Testing

**Goal:** Test FastAPI endpoints with full request/response cycle

**Setup:**
```python
# conftest.py
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Test client for API endpoints."""
    return TestClient(app)
```

**Pattern:**
```python
def test_api_endpoint(client: TestClient, test_data):
    # Arrange
    payload = {...}
    headers = {...}

    # Act
    response = client.post("/api/endpoint", json=payload, headers=headers)

    # Assert
    assert response.status_code == 201
    data = response.json()
    assert data["field"] == expected_value
```

**Example: Testing Applications API**

```python
class TestApplicationsAPICreate:
    """Tests for POST /api/applications endpoint."""

    def test_create_application_success(
        self, client: TestClient, test_user: User, test_job: Job
    ):
        """Test creating application with valid data."""
        payload = {
            "job_id": test_job.id,
            "status": "draft",
            "notes": "Test application"
        }
        headers = {"user-id": str(test_user.id)}  # TODO: Replace with JWT

        response = client.post("/api/applications", json=payload, headers=headers)

        assert response.status_code == 201
        data = response.json()
        assert data["job_id"] == test_job.id
        assert data["status"] == "draft"
        assert data["notes"] == "Test application"
        assert "id" in data
        assert "created_at" in data

    def test_create_application_invalid_job(
        self, client: TestClient, test_user: User
    ):
        """Test creating application with invalid job ID."""
        payload = {
            "job_id": 99999,
            "status": "draft",
        }
        headers = {"user-id": str(test_user.id)}

        response = client.post("/api/applications", json=payload, headers=headers)

        assert response.status_code == 400
        assert "not found" in response.json()["detail"].lower()

    def test_create_application_missing_required_field(
        self, client: TestClient, test_user: User
    ):
        """Test validation of required fields."""
        payload = {"status": "draft"}  # Missing job_id
        headers = {"user-id": str(test_user.id)}

        response = client.post("/api/applications", json=payload, headers=headers)

        assert response.status_code == 422  # Validation error


class TestApplicationsAPIRead:
    """Tests for GET /api/applications endpoints."""

    def test_list_applications(
        self, client: TestClient, test_user: User, test_applications: list
    ):
        """Test listing all user applications."""
        headers = {"user-id": str(test_user.id)}

        response = client.get("/api/applications", headers=headers)

        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) >= len(test_applications)

    def test_filter_applications_by_status(
        self, client: TestClient, test_user: User
    ):
        """Test filtering applications by status."""
        headers = {"user-id": str(test_user.id)}

        response = client.get(
            "/api/applications?status=draft",
            headers=headers
        )

        assert response.status_code == 200
        data = response.json()
        assert all(app["status"] == "draft" for app in data)

    def test_get_single_application(
        self, client: TestClient, test_user: User, test_application
    ):
        """Test getting single application by ID."""
        headers = {"user-id": str(test_user.id)}

        response = client.get(
            f"/api/applications/{test_application.id}",
            headers=headers
        )

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == test_application.id
        assert "job" in data  # Eager loaded
        assert "company" in data["job"]  # Nested eager loaded
```

---

## Testing Best Practices

### 1. Use Descriptive Test Names

✅ **Good:**
```python
async def test_create_application_submitted_sets_applied_date()
async def test_invalid_transition_draft_to_offer_raises_error()
async def test_delete_application_performs_soft_delete()
```

❌ **Bad:**
```python
async def test_create()
async def test_status()
async def test_delete()
```

### 2. One Assert Per Concept

✅ **Good:**
```python
async def test_create_application_sets_defaults():
    application = await service.create_application(db, job_id, user_id)

    # Test default status
    assert application.status == ApplicationStatus.DRAFT
    assert application.applied_date is None
    assert application.is_active is True
```

❌ **Bad:**
```python
async def test_create_application():
    # Testing too many unrelated things
    assert application.status == ApplicationStatus.DRAFT
    assert len(await service.get_applications(db, user_id)) > 0
    assert application.created_at < datetime.now()
    # ... 20 more asserts
```

### 3. Test Edge Cases

```python
# Test boundary conditions
async def test_salary_filter_exactly_at_minimum()
async def test_salary_filter_exactly_at_maximum()
async def test_empty_result_set()

# Test error conditions
async def test_create_with_null_required_field()
async def test_update_nonexistent_record()
async def test_invalid_enum_value()

# Test state transitions
async def test_transition_from_each_valid_status()
async def test_terminal_statuses_cannot_transition()
```

### 4. Use Fixtures for Test Data

✅ **Good:**
```python
@pytest.fixture
async def test_application_draft(db_session, test_job, test_user):
    """Create a draft application for testing."""
    service = ApplicationService()
    return await service.create_application(
        db=db_session,
        job_id=test_job.id,
        user_id=test_user.id,
        status=ApplicationStatus.DRAFT,
    )

async def test_update_draft_to_submitted(test_application_draft):
    # Fixture provides clean test data
    ...
```

❌ **Bad:**
```python
async def test_update_draft_to_submitted(db_session):
    # Recreating test data in every test
    user = User(...)
    db_session.add(user)
    company = Company(...)
    db_session.add(company)
    job = Job(...)
    # ... many more lines
```

### 5. Clean Up Test Data

```python
@pytest.fixture
async def test_application(db_session):
    """Create test application (auto-cleaned after test)."""
    app = Application(...)
    db_session.add(app)
    await db_session.commit()
    yield app
    # Cleanup happens automatically with transaction rollback
```

### 6. Test Async Code Properly

✅ **Good:**
```python
@pytest.mark.asyncio
async def test_async_service():
    result = await service.async_method()
    assert result is not None
```

❌ **Bad:**
```python
def test_async_service():  # Missing @pytest.mark.asyncio
    result = service.async_method()  # Missing await
    assert result is not None
```

---

## Database Testing Strategy

### Strategy: PostgreSQL for Tests

**Rationale:**
- Matches production database exactly
- No ARRAY type compatibility issues
- Proper transaction support
- Real database constraints

**Setup:**
```python
# conftest.py
import pytest
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

TEST_DATABASE_URL = "postgresql+asyncpg://postgres:test@localhost:5432/test_db"

@pytest.fixture(scope="session")
async def test_engine():
    """Create test database engine."""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)
    yield engine
    await engine.dispose()

@pytest.fixture(scope="function")
async def db_session(test_engine):
    """Create fresh database session for each test."""
    async_session = sessionmaker(
        test_engine,
        class_=AsyncSession,
        expire_on_commit=False
    )

    async with async_session() as session:
        async with session.begin():
            yield session
            await session.rollback()  # Rollback after each test
```

### Transaction Rollback Pattern

Each test runs in a transaction that's rolled back:

```python
async def test_create_application(db_session):
    # Changes made here
    application = await service.create_application(...)

    # Test assertions
    assert application.id is not None

    # Automatic rollback after test completes
    # Database returns to clean state
```

**Benefits:**
- Fast (no need to delete test data)
- Isolated (tests don't affect each other)
- Clean (database state resets automatically)

### Database Fixtures

```python
@pytest_asyncio.fixture
async def test_company(db_session: AsyncSession):
    """Create test company."""
    company = Company(
        name="Test Company",
        domain="testcompany.com",
        industry="Technology",
        size="50-200",
    )
    db_session.add(company)
    await db_session.flush()  # Get ID without committing
    return company

@pytest_asyncio.fixture
async def test_job(db_session: AsyncSession, test_company):
    """Create test job."""
    job = Job(
        company_id=test_company.id,
        title="Software Engineer",
        location="San Francisco, CA",
        salary_min=100000,
        salary_max=150000,
        remote=True,
    )
    db_session.add(job)
    await db_session.flush()
    return job

@pytest_asyncio.fixture
async def test_user(db_session: AsyncSession):
    """Create test user."""
    user = User(
        email="test@example.com",
        username="testuser",
    )
    db_session.add(user)
    await db_session.flush()
    return user
```

---

## Mocking & Fixtures

### When to Mock

**Mock External Services:**
- HTTP API calls (JobSpy, Claude API)
- Email services
- File system operations
- Third-party integrations

**Don't Mock:**
- Your own code
- Database operations (use test database)
- Simple utilities

### Mocking External APIs

```python
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_search_jobs_via_jobspy():
    """Test job search with mocked JobSpy API."""
    mock_results = [
        {"title": "Engineer", "company": "Test Corp", ...},
        {"title": "Developer", "company": "Another Co", ...},
    ]

    with patch('src.scrapers.jobspy_client.scrape_jobs') as mock_scrape:
        mock_scrape.return_value = mock_results

        service = JobSearchService()
        results = await service.search_jobs(
            query="python developer",
            location="San Francisco"
        )

        assert len(results) == 2
        mock_scrape.assert_called_once_with(
            site_name=["indeed", "linkedin"],
            search_term="python developer",
            location="San Francisco"
        )
```

### Fixture Scopes

```python
@pytest.fixture(scope="session")
def app():
    """App instance (created once per test session)."""
    return create_app()

@pytest.fixture(scope="module")
def client(app):
    """Test client (created once per test module)."""
    return TestClient(app)

@pytest.fixture(scope="function")  # Default
async def db_session():
    """Fresh database session (created for each test function)."""
    ...
```

---

## Coverage Targets

### Overall Targets

| Component | Target Coverage | Priority |
|-----------|----------------|----------|
| **Service Layer** | 90-100% | 🔴 Critical |
| **API Endpoints** | 95%+ | 🔴 Critical |
| **Models** | 85%+ | 🟡 High |
| **Utilities** | 90%+ | 🟡 High |
| **Scrapers** | 70%+ | 🟢 Medium |

### Running Coverage

```bash
# Generate coverage report
pytest tests/ --cov=src --cov-report=html

# View coverage in browser
open htmlcov/index.html

# Show missing lines
pytest tests/ --cov=src --cov-report=term-missing
```

### Coverage Configuration

```toml
# pyproject.toml
[tool.pytest.ini_options]
addopts = [
    "--cov=src",
    "--cov-report=term-missing",
    "--cov-report=html",
    "--cov-fail-under=80",  # Fail if coverage < 80%
]
```

---

## Implementation Examples

### Example 1: Complete Service Test File

```python
# tests/test_job_search_service.py

import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from unittest.mock import patch

from src.services.job_search_service import JobSearchService
from src.models.database import Job, Company


class TestJobSearchServiceSearch:
    """Tests for external job searching."""

    @pytest.mark.asyncio
    async def test_search_jobs_basic_query(self, db_session: AsyncSession):
        """Test basic job search with mock JobSpy."""
        mock_jobs = [
            {"title": "Engineer", "company": "Test Corp", "location": "SF"},
            {"title": "Developer", "company": "Another Co", "location": "NYC"},
        ]

        with patch('src.scrapers.jobspy_client.search') as mock:
            mock.return_value = mock_jobs

            service = JobSearchService()
            results = await service.search_jobs(
                db=db_session,
                query="python",
                location="San Francisco"
            )

            assert len(results) >= 2
            assert all(isinstance(job, Job) for job in results)

    @pytest.mark.asyncio
    async def test_search_deduplicates_jobs(self, db_session: AsyncSession):
        """Test that duplicate jobs are not created."""
        # First search
        service = JobSearchService()
        with patch('src.scrapers.jobspy_client.search') as mock:
            mock.return_value = [
                {"title": "Engineer", "company": "Test Corp", "url": "http://test.com/job1"}
            ]
            await service.search_jobs(db=db_session, query="python")

        # Second search with same job
        with patch('src.scrapers.jobspy_client.search') as mock:
            mock.return_value = [
                {"title": "Engineer", "company": "Test Corp", "url": "http://test.com/job1"}
            ]
            results = await service.search_jobs(db=db_session, query="python")

        # Should only have one job
        all_jobs = await service.get_jobs(db=db_session)
        assert len([j for j in all_jobs if j.url == "http://test.com/job1"]) == 1


class TestJobSearchServiceDatabase:
    """Tests for database operations."""

    @pytest.mark.asyncio
    async def test_get_job_by_id(
        self, db_session: AsyncSession, test_job: Job
    ):
        """Test retrieving single job."""
        service = JobSearchService()

        result = await service.get_job(db=db_session, job_id=test_job.id)

        assert result is not None
        assert result.id == test_job.id
        assert result.title == test_job.title

    @pytest.mark.asyncio
    async def test_list_jobs_with_pagination(
        self, db_session: AsyncSession, test_jobs: list[Job]
    ):
        """Test listing jobs with pagination."""
        service = JobSearchService()

        # Get first page
        page1 = await service.get_jobs(db=db_session, skip=0, limit=2)
        assert len(page1) == 2

        # Get second page
        page2 = await service.get_jobs(db=db_session, skip=2, limit=2)
        assert len(page2) <= 2

        # Ensure no overlap
        page1_ids = {j.id for j in page1}
        page2_ids = {j.id for j in page2}
        assert len(page1_ids & page2_ids) == 0

    @pytest.mark.asyncio
    async def test_filter_jobs_by_salary(
        self, db_session: AsyncSession
    ):
        """Test filtering jobs by salary range."""
        # Create jobs with different salaries
        service = JobSearchService()

        results = await service.get_jobs(
            db=db_session,
            salary_min=80000,
            salary_max=120000
        )

        for job in results:
            if job.salary_min:
                assert job.salary_min >= 80000
            if job.salary_max:
                assert job.salary_max <= 120000
```

---

## Common Patterns & Anti-patterns

### ✅ Good Patterns

**1. Use Parametrize for Similar Tests**
```python
@pytest.mark.parametrize("status,expected_applied_date", [
    (ApplicationStatus.DRAFT, None),
    (ApplicationStatus.SUBMITTED, "not_none"),
    (ApplicationStatus.SCREENING, "not_none"),
])
async def test_applied_date_by_status(status, expected_applied_date, db_session):
    app = await service.create_application(db_session, status=status)

    if expected_applied_date == "not_none":
        assert app.applied_date is not None
    else:
        assert app.applied_date is None
```

**2. Use Context Managers for Expected Errors**
```python
with pytest.raises(ValueError, match="Invalid status transition"):
    await service.update_status(...)
```

**3. Test Both Success and Failure Paths**
```python
class TestAuthentication:
    async def test_login_success(self): ...
    async def test_login_invalid_password(self): ...
    async def test_login_nonexistent_user(self): ...
    async def test_login_locked_account(self): ...
```

### ❌ Anti-patterns

**1. Testing Implementation Details**
```python
# BAD: Testing internal method calls
def test_create_application():
    with patch.object(service, '_validate_job') as mock:
        service.create_application(...)
        mock.assert_called_once()  # Testing implementation!
```

**2. Interdependent Tests**
```python
# BAD: Test B depends on Test A
def test_a_create_user():
    global user_id
    user_id = create_user()

def test_b_update_user():
    update_user(user_id)  # Breaks if test_a doesn't run!
```

**3. Excessive Mocking**
```python
# BAD: Mocking everything
with patch('service.method1'), \
     patch('service.method2'), \
     patch('service.method3'):
    # What are we actually testing?
    result = service.do_something()
```

**4. Magic Numbers**
```python
# BAD
assert len(results) == 5  # Why 5?

# GOOD
EXPECTED_JOB_COUNT = 5  # Number of test jobs created
assert len(results) == EXPECTED_JOB_COUNT
```

---

## Next Steps

1. **Set up PostgreSQL test database**
   ```bash
   docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=test -e POSTGRES_DB=test_db postgres:15
   ```

2. **Run existing tests**
   ```bash
   cd backend && pytest tests/ -v
   ```

3. **Implement JobSearchService tests** (Week 1, Days 3-5)
   - Follow patterns from `test_application_service.py`
   - Aim for 90%+ coverage
   - 20-25 tests expected

4. **Add API integration tests** (Week 2, Days 1-3)
   - Use FastAPI TestClient
   - Test all endpoints
   - 40-50 tests expected

5. **Monitor coverage**
   ```bash
   pytest tests/ --cov=src --cov-report=html
   ```

---

## Resources

- [pytest Documentation](https://docs.pytest.org/)
- [pytest-asyncio](https://pytest-asyncio.readthedocs.io/)
- [FastAPI Testing](https://fastapi.tiangolo.com/tutorial/testing/)
- [SQLAlchemy Testing](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)
- [Testing Best Practices](https://docs.python-guide.org/writing/tests/)

---

**Version:** 1.0
**Last Updated:** November 22, 2025
**Status:** Ready for implementation
