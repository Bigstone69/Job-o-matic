# Job-o-matic - Quick Task Reference

**Current Phase:** Phase 2 - Job Search & Management
**Next Task:** BE-DB-001

## 🎯 Immediate Next Steps (This Week)

### 1. BE-DB-001: Create Database Migration 🔴
**Priority:** P0 Critical | **Time:** 1 hour
```bash
cd backend
alembic revision --autogenerate -m "initial schema"
alembic upgrade head
```
**Outcome:** All database tables created

---

### 2. BE-JOB-001: JobSpy Integration 🔴
**Priority:** P0 Critical | **Time:** 4 hours

**Research:** https://github.com/Bunsly/JobSpy

**Create:** `backend/src/scrapers/jobspy_client.py`
```python
class JobSpyClient:
    async def search(self, query: str, location: str, **filters) -> List[dict]
    async def get_job_details(self, job_id: str) -> dict
```

**Test:** `backend/tests/test_jobspy_client.py`

**Acceptance:**
- ✅ Can search jobs from LinkedIn, Indeed, Glassdoor
- ✅ Returns structured data
- ✅ Error handling for rate limits
- ✅ Logging enabled

---

### 3. BE-SVC-001: Job Search Service 🔴
**Priority:** P0 Critical | **Time:** 6 hours

**Create:** `backend/src/services/job_search_service.py`
```python
class JobSearchService:
    async def search_jobs(query, location, filters) -> List[Job]
    async def normalize_job(raw_data) -> Job
    async def deduplicate(jobs) -> List[Job]
    async def save_job(job_data) -> Job
```

**Features:**
- Data normalization (external format → Job model)
- Duplicate detection
- Company auto-creation
- Caching (5 min TTL)
- Save to database

**Test:** `backend/tests/test_job_search_service.py`

---

### 4. BE-API-001: Job Search API Endpoints 🔴
**Priority:** P0 Critical | **Time:** 4 hours

**Create:** `backend/src/api/jobs.py`

**Endpoints:**
```python
POST   /api/v1/jobs/search      # Search jobs
GET    /api/v1/jobs             # List saved jobs
GET    /api/v1/jobs/{id}        # Get job detail
POST   /api/v1/jobs             # Manual job entry
```

**Create:** `backend/src/api/schemas/job_schemas.py`

**Test:** `backend/tests/test_api_jobs.py`

---

### 5. FE-API-001: Frontend API Client 🟠
**Priority:** P1 High | **Time:** 3 hours

**Create:**
- `frontend/src/services/api.ts` - Axios instance
- `frontend/src/services/jobsApi.ts` - Jobs API client
- `frontend/src/hooks/useJobs.ts` - React Query hooks
- `frontend/src/types/job.ts` - TypeScript types

**Example:**
```typescript
export function useSearchJobs() {
  return useMutation({
    mutationFn: jobsApi.searchJobs,
  })
}
```

---

## 📊 Week 2 Sprint Plan

| Day | Task ID | Task | Hours |
|-----|---------|------|-------|
| Mon | BE-DB-001 | Database Migration | 1 |
| Mon | BE-JOB-001 | JobSpy Integration | 4 |
| Tue | BE-SVC-001 | Job Search Service | 6 |
| Wed | BE-API-001 | Job Search Endpoints | 4 |
| Wed | FE-API-001 | Frontend API Client | 3 |
| Thu | FE-UI-001 | Job UI Components | 5 |
| Fri | FE-PAGE-001 | Job Search Page | 4 |
| Fri | TEST-001 | Backend Tests | 4 |

**Total:** ~31 hours (realistic for 1 week)

---

## 🔍 Current Progress

### ✅ Completed (Phase 1)
- [x] Project structure
- [x] Database models (9 models)
- [x] FastAPI application
- [x] React frontend setup
- [x] Docker configuration
- [x] All documentation

### 🚧 In Progress (Phase 2)
- [ ] Database migration
- [ ] Job search implementation
- [ ] Frontend integration

### 📋 Up Next (Phase 3)
- [ ] Application tracking
- [ ] Status management
- [ ] Timeline views

---

## 🎯 Definition of Done

Each task is "done" when:
- ✅ Code written and follows style guide
- ✅ Tests written and passing
- ✅ Linting passes (ruff/ESLint)
- ✅ Type checking passes (mypy/TypeScript)
- ✅ Code reviewed (self-review minimum)
- ✅ Committed with conventional commit message
- ✅ Documentation updated if needed

---

## 🐛 Known Issues / Tech Debt

*(To be updated as development progresses)*

---

## 💡 Quick Commands

### Backend
```bash
# Run server
cd backend
uvicorn src.main:app --reload

# Run tests
pytest

# Check code quality
ruff check src/
black src/
mypy src/

# Database migration
alembic revision --autogenerate -m "description"
alembic upgrade head
```

### Frontend
```bash
# Run dev server
cd frontend
npm run dev

# Run tests
npm run test

# Check code quality
npm run lint
npm run type-check
npm run format
```

### Docker
```bash
# Start PostgreSQL
docker-compose up -d postgres

# View logs
docker logs jobomatic-db

# Stop all
docker-compose down
```

---

## 📚 Reference Documents

- **Full Roadmap:** [docs/development-roadmap.md](docs/development-roadmap.md)
- **Architecture:** [docs/implementation-plan.md](docs/implementation-plan.md)
- **Tech Stack:** [docs/tech-stack-decision.md](docs/tech-stack-decision.md)
- **Job Search Strategy:** [docs/job-search-strategy.md](docs/job-search-strategy.md)
- **MCP Research:** [docs/mcp-protocol-research.md](docs/mcp-protocol-research.md)

---

## 🎯 Success Metrics

### Phase 2 Success (Week 2-4)
- [ ] Can search jobs from 3+ sources
- [ ] Search returns results in < 3 seconds
- [ ] Jobs display in frontend
- [ ] Can manually add jobs
- [ ] All backend tests passing (>80% coverage)

### MVP Success (Week 8)
- [ ] Can search and save jobs
- [ ] Can track applications through stages
- [ ] Can generate AI cover letters
- [ ] MCP server working with Claude
- [ ] All core features functional

---

**Last Updated:** November 22, 2025
**Next Review:** After completing Phase 2
