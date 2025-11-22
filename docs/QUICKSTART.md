# Job-o-matic Quick Start Guide

**Get up and running with Job-o-matic in 10 minutes!**

Last Updated: November 22, 2025

---

## Prerequisites

Ensure you have the following installed:

- **Python 3.11+** with uv package manager
- **Node.js 20+** with npm
- **PostgreSQL 15+** (or Docker)
- **Git**

---

## Quick Setup (Development)

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Job-o-matic
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Install dependencies with uv
uv sync

# Set up environment variables
cp .env.example .env
# Edit .env with your database credentials and API keys

# Run database migrations (if Alembic is configured)
# alembic upgrade head

# Start the backend server
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`
API documentation at `http://localhost:8000/docs`

### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Set up environment variables
# Create .env file with:
echo "VITE_API_BASE_URL=http://localhost:8000" > .env

# Start the development server
npm run dev
```

The frontend will be available at `http://localhost:5173`

### 4. Verify Installation

Visit `http://localhost:5173` in your browser. You should see the Job-o-matic dashboard.

---

## Project Structure

```
Job-o-matic/
├── backend/
│   ├── src/
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── models/
│   │   │   ├── database.py      # SQLAlchemy models
│   │   │   └── session.py       # Database session management
│   │   ├── api/
│   │   │   ├── jobs.py          # Job endpoints
│   │   │   ├── applications.py  # Application endpoints
│   │   │   └── schemas/         # Pydantic request/response schemas
│   │   ├── services/
│   │   │   ├── job_search_service.py      # Job search business logic
│   │   │   └── application_service.py     # Application management
│   │   └── scrapers/
│   │       └── jobspy_client.py # JobSpy API integration
│   ├── tests/                   # Unit and integration tests
│   ├── pyproject.toml           # Python dependencies and config
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── main.tsx             # React app entry point
│   │   ├── App.tsx              # Main app component
│   │   ├── pages/               # Page components
│   │   ├── components/          # Reusable UI components
│   │   ├── hooks/               # React Query hooks
│   │   ├── api/                 # API client functions
│   │   └── types/               # TypeScript type definitions
│   ├── package.json             # Node dependencies
│   └── vite.config.ts           # Vite configuration
│
├── docs/                        # Comprehensive documentation
├── scripts/                     # Utility scripts
└── README.md                    # Project overview
```

---

## Available Features

### ✅ Implemented (Phase 1-3)

**Phase 1: Foundation**
- Database models (Jobs, Applications, Companies, Users)
- SQLAlchemy ORM with async support
- FastAPI backend with auto-generated docs
- React frontend with TypeScript
- Docker development environment

**Phase 2: Job Search**
- JobSpy API integration for multi-platform search
- Job search with filters (location, salary, remote, etc.)
- Job listing and detail views
- Manual job entry
- Company management

**Phase 3: Application Tracking**
- Application CRUD operations (Create, Read, Update, Delete)
- Status management (Draft → Submitted → Screening → Interview → Offer)
- Status history tracking with audit trail
- Application statistics and analytics
- Activity logging
- Optimistic UI updates with React Query

### 🚧 In Progress

**Testing Infrastructure**
- ✅ 26 ApplicationService unit tests (100% coverage)
- ✅ Automated testing script (`scripts/test_and_index_bugs.py`)
- ✅ Type checking: 100% clean (backend + frontend)
- 📝 JobSearchService unit tests (planned)
- 📝 API integration tests (planned)
- 📝 E2E tests with Playwright (planned)

### 📋 Planned (Phase 4-8)

**Phase 4: Authentication & Authorization**
- User registration and login
- JWT token-based authentication
- Password hashing with bcrypt
- Protected API endpoints

**Phase 5: LLM Integration**
- Claude API integration for cover letters
- Ollama support for local models
- Cover letter generation and management
- Job requirement analysis

**Phase 6: MCP Server**
- FastMCP server implementation
- MCP tools for Claude Desktop
- Resource exposure (jobs, applications)
- Prompt templates

**Phase 7: Dashboard & Analytics**
- Application pipeline visualization
- Response rate tracking
- Timeline views
- Dark mode

**Phase 8: Production Deployment**
- Docker production images
- PostgreSQL production setup
- Environment configuration
- Monitoring and logging

---

## Development Workflow

### Running Tests

**Backend Tests:**
```bash
cd backend

# Run all unit tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_application_service.py -v

# Run automated test suite
cd ..
python scripts/test_and_index_bugs.py
```

**Frontend Tests:**
```bash
cd frontend

# Type checking
npm run type-check

# Linting
npm run lint

# Unit tests (when configured)
npm run test
```

### Code Quality

**Backend:**
```bash
cd backend

# Linting with ruff
ruff check src/

# Auto-fix issues
ruff check src/ --fix

# Type checking with mypy
mypy src/
```

**Frontend:**
```bash
cd frontend

# Linting with ESLint
npm run lint

# Type checking
npm run type-check
```

### Database Migrations (when using Alembic)

```bash
cd backend

# Create a new migration
alembic revision --autogenerate -m "Description of changes"

# Apply migrations
alembic upgrade head

# Rollback last migration
alembic downgrade -1
```

---

## API Endpoints

### Jobs API

```
GET    /api/jobs              # List jobs with filters
GET    /api/jobs/{id}         # Get job details
POST   /api/jobs/search       # Search jobs via JobSpy
POST   /api/jobs              # Create manual job entry
DELETE /api/jobs/{id}         # Delete job
```

### Applications API

```
GET    /api/applications              # List applications
GET    /api/applications/stats        # Get statistics
GET    /api/applications/{id}         # Get application details
POST   /api/applications              # Create application
PUT    /api/applications/{id}         # Update application
PUT    /api/applications/{id}/status  # Update status
DELETE /api/applications/{id}         # Delete application
GET    /api/applications/{id}/history # Get status history
```

**API Documentation:** `http://localhost:8000/docs` (Swagger UI)

---

## Environment Variables

### Backend (.env)

```bash
# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/jobomatic

# Optional: Claude API (for future cover letter generation)
ANTHROPIC_API_KEY=your_api_key_here

# Optional: Ollama (for local LLM)
OLLAMA_HOST=http://localhost:11434
```

### Frontend (.env)

```bash
# API Base URL
VITE_API_BASE_URL=http://localhost:8000
```

---

## Common Issues & Solutions

### Issue: Database connection errors

**Solution:**
1. Ensure PostgreSQL is running: `pg_isready`
2. Check credentials in `backend/.env`
3. Verify database exists: `psql -l`
4. Create database if needed: `createdb jobomatic`

### Issue: Frontend can't connect to API

**Solution:**
1. Verify backend is running on port 8000
2. Check `VITE_API_BASE_URL` in `frontend/.env`
3. Check CORS settings in `backend/src/main.py`

### Issue: Import errors in backend

**Solution:**
1. Ensure you're in the correct directory
2. Activate virtual environment: `uv sync`
3. Reinstall dependencies: `uv sync --reinstall`

### Issue: TypeScript errors

**Solution:**
1. Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`
2. Check `tsconfig.json` configuration
3. Verify all type definitions are installed

---

## Testing Infrastructure

### Current Test Coverage

| Component | Tests | Coverage | Status |
|-----------|-------|----------|--------|
| ApplicationService | 26 | 100% | ✅ Complete |
| JobSearchService | 0 | 0% | 📝 Planned |
| API Endpoints | 0 | 0% | 📝 Planned |
| Frontend Components | 0 | 0% | 📝 Planned |
| **Overall** | **26** | **~15%** | 🚧 In Progress |

**Target:** 80% overall coverage (90% for critical paths)

### Automated Testing

Run comprehensive automated test suite:

```bash
python scripts/test_and_index_bugs.py
```

This script runs:
- Backend linting (ruff)
- Backend type checking (mypy)
- Frontend type checking (tsc)
- Backend unit tests (pytest)
- Security vulnerability scanning
- Code quality analysis

**Current Results:**
- Total Issues: 27 (down from 757!)
- MEDIUM Priority: 0 (100% fixed!)
- Backend Type Errors: 0 (100% clean!)
- Frontend Type Errors: 0 (100% clean!)

---

## Code Quality Metrics

### Type Safety
- ✅ Backend: 100% type-safe (mypy strict mode)
- ✅ Frontend: 100% type-safe (TypeScript strict mode)
- ✅ SQLAlchemy mypy plugin configured
- ✅ Pydantic mypy plugin configured

### Code Style
- ✅ Backend: Ruff for linting and formatting
- ✅ Frontend: ESLint + Prettier
- ✅ Import sorting automated
- ✅ Modern Python 3.10+ type hints

### Testing
- ✅ pytest for backend unit tests
- ✅ pytest-asyncio for async tests
- ✅ pytest-cov for coverage reporting
- 📝 Vitest for frontend tests (planned)
- 📝 Playwright for E2E tests (planned)

---

## Next Steps

### For New Contributors

1. **Set up development environment** (follow steps above)
2. **Read the documentation:**
   - `docs/issue-fix-and-testing-strategy.md` - Testing plan
   - `docs/session-summary-phase3-completion.md` - Latest progress
   - `docs/implementation-plan.md` - Overall architecture
3. **Run the automated tests** to verify your setup
4. **Pick a task** from the testing strategy document
5. **Write tests** following the patterns in `backend/tests/`

### For Project Owners

1. **Review Phase 3 completion:**
   - Application tracking fully implemented
   - 95.6% issue reduction achieved
   - 100% type safety established
2. **Plan Phase 4:** Authentication & Authorization
3. **Review testing strategy:** See `docs/issue-fix-and-testing-strategy.md`
4. **Decide on next priorities:**
   - Continue backend testing (Week 1-2 of testing plan)?
   - Begin Phase 4 authentication?
   - Focus on production deployment preparation?

---

## Resources

### Documentation
- [Testing Strategy](issue-fix-and-testing-strategy.md) - Comprehensive testing plan
- [Session Summary](session-summary-phase3-completion.md) - Latest session progress
- [Implementation Plan](implementation-plan.md) - Overall architecture
- [Phase 3 Plan](phase3-plan.md) - Application tracking design

### API Documentation
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### External Resources
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [TanStack Query](https://tanstack.com/query/latest)

---

## Support

For issues or questions:
1. Check this guide for common issues
2. Review existing documentation in `docs/`
3. Check the automated test report for current status
4. Open an issue in the repository

---

**Happy Coding! 🚀**

Built with ❤️ using FastAPI, React, and PostgreSQL
