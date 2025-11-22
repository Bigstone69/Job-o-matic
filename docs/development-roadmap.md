# Job-o-matic Development Roadmap

**Version:** 1.0
**Last Updated:** November 22, 2025
**Status:** Phase 1 Complete - Planning Phase 2-8

## Table of Contents

1. [Priority Legend](#priority-legend)
2. [Category Index](#category-index)
3. [Dependency Map](#dependency-map)
4. [Phase 2: Job Search & Management](#phase-2-job-search--management)
5. [Phase 3: Application Tracking](#phase-3-application-tracking)
6. [Phase 4: LLM Integration](#phase-4-llm-integration)
7. [Phase 5: MCP Server](#phase-5-mcp-server)
8. [Phase 6: Dashboard & Analytics](#phase-6-dashboard--analytics)
9. [Phase 7: Testing & Quality](#phase-7-testing--quality)
10. [Phase 8: Deployment & Polish](#phase-8-deployment--polish)

---

## Priority Legend

| Priority | Label | Description | Timeline |
|----------|-------|-------------|----------|
| **P0** | 🔴 Critical | Blocking issues, core functionality | Immediate |
| **P1** | 🟠 High | Essential features for MVP | Week 2-4 |
| **P2** | 🟡 Medium | Important but not blocking | Week 5-8 |
| **P3** | 🟢 Low | Nice-to-have, polish features | Week 9+ |

## Category Index

### Backend Categories
- **[BE-DB]** - Database & Models
- **[BE-API]** - REST API Endpoints
- **[BE-SVC]** - Business Logic Services
- **[BE-LLM]** - LLM Integration
- **[BE-MCP]** - MCP Server
- **[BE-JOB]** - Job Search Engine

### Frontend Categories
- **[FE-UI]** - UI Components
- **[FE-PAGE]** - Pages & Routes
- **[FE-STATE]** - State Management
- **[FE-API]** - API Integration

### Infrastructure Categories
- **[INFRA]** - Docker, Deployment
- **[CONFIG]** - Configuration Management

### Quality Categories
- **[TEST]** - Testing
- **[DOC]** - Documentation
- **[QA]** - Code Quality & Standards

---

## Dependency Map

```
Phase 2 (Job Search)
├─► BE-DB-001 (Database Migration)
├─► BE-SVC-001 (Job Search Service)
│   └─► BE-JOB-001 (JobSpy Integration)
│       └─► BE-API-001 (Job Search Endpoints)
│           └─► FE-API-001 (API Client)
│               └─► FE-UI-001 (Job Components)
│                   └─► FE-PAGE-001 (Job Search Page)

Phase 3 (Applications)
├─► BE-SVC-002 (Application Service)
│   └─► BE-API-002 (Application Endpoints)
│       └─► FE-API-002 (Application Client)
│           └─► FE-UI-002 (Application Components)

Phase 4 (LLM)
├─► BE-LLM-001 (LLM Provider Interface)
│   ├─► BE-LLM-002 (Claude Integration)
│   ├─► BE-LLM-003 (Ollama Integration)
│   └─► BE-SVC-003 (Cover Letter Service)

Phase 5 (MCP)
└─► BE-MCP-001 (MCP Server Foundation)
    └─► BE-MCP-002-007 (6 MCP Tools)

Phase 6 (Dashboard)
└─► Depends on: Phase 2, 3 data availability

Phase 7 (Testing)
└─► Continuous throughout all phases

Phase 8 (Deployment)
└─► Final phase, depends on all above
```

---

## Phase 2: Job Search & Management
**Timeline:** Week 2-4 | **Status:** Next Up

### 2.1 Database Foundation
**Priority: P0 🔴 | Dependencies: None**

#### BE-DB-001: Create Initial Database Migration
- **Priority:** P0 🔴
- **Effort:** 1 hour
- **Dependencies:** None
- **Tasks:**
  ```bash
  # Create migration
  alembic revision --autogenerate -m "initial schema"

  # Review migration file
  # Apply migration
  alembic upgrade head

  # Verify tables created
  ```
- **Acceptance Criteria:**
  - [ ] All 9 tables created in PostgreSQL
  - [ ] Indexes created correctly
  - [ ] Foreign keys working
  - [ ] Migration can rollback successfully
- **Files:** `backend/alembic/versions/XXXX_initial_schema.py`

#### BE-DB-002: Create Database Seed Data
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-DB-001
- **Tasks:**
  - Create seed script for development
  - Add sample users (1-2)
  - Add sample companies (10-15)
  - Add sample jobs (20-30)
  - Add sample applications (5-10)
- **Acceptance Criteria:**
  - [ ] Seed script runs successfully
  - [ ] Data is realistic and useful for testing
  - [ ] Idempotent (can run multiple times)
- **Files:** `backend/scripts/seed_database.py`

---

### 2.2 Job Search Backend
**Priority: P0 🔴 | Dependencies: BE-DB-001**

#### BE-JOB-001: JobSpy API Integration
- **Priority:** P0 🔴
- **Effort:** 4 hours
- **Dependencies:** BE-DB-001
- **Tasks:**
  1. Research JobSpy API/library (https://github.com/Bunsly/JobSpy)
  2. Create JobSpy client wrapper class
  3. Implement search method
  4. Add error handling and retries
  5. Add logging
- **Implementation:**
  ```python
  # backend/src/scrapers/jobspy_client.py
  class JobSpyClient:
      async def search(self, query: str, location: str, **filters) -> List[dict]
      async def get_job_details(self, job_id: str) -> dict
  ```
- **Acceptance Criteria:**
  - [ ] Can search jobs by query and location
  - [ ] Returns structured job data
  - [ ] Handles errors gracefully (rate limits, network)
  - [ ] Logging for all operations
  - [ ] Works with multiple sources (LinkedIn, Indeed, etc.)
- **Files:**
  - `backend/src/scrapers/jobspy_client.py`
  - `backend/tests/test_jobspy_client.py`

#### BE-SVC-001: Job Search Service
- **Priority:** P0 🔴
- **Effort:** 6 hours
- **Dependencies:** BE-JOB-001
- **Tasks:**
  1. Create JobSearchService class
  2. Implement data normalization (external → internal format)
  3. Implement deduplication logic
  4. Add caching layer (Redis or in-memory)
  5. Create company matching/creation logic
  6. Save jobs to database
- **Implementation:**
  ```python
  # backend/src/services/job_search_service.py
  class JobSearchService:
      async def search_jobs(query, location, filters) -> List[Job]
      async def normalize_job(raw_data) -> Job
      async def deduplicate(jobs) -> List[Job]
      async def save_job(job_data) -> Job
  ```
- **Acceptance Criteria:**
  - [ ] Searches return normalized Job objects
  - [ ] Duplicate jobs filtered out
  - [ ] Companies auto-created if not exist
  - [ ] Search results cached (5 min TTL)
  - [ ] Jobs saved to database
  - [ ] Performance < 3 seconds for search
- **Files:**
  - `backend/src/services/job_search_service.py`
  - `backend/tests/test_job_search_service.py`

#### BE-SVC-002: Manual Job Entry Service
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-SVC-001
- **Tasks:**
  1. Create method for manual job creation
  2. Validate required fields
  3. Support partial data entry
  4. Company lookup/creation
- **Implementation:**
  ```python
  class JobSearchService:
      async def create_manual_job(job_data: dict) -> Job
  ```
- **Acceptance Criteria:**
  - [ ] Can create job with minimal data (title, company, url)
  - [ ] Optional fields handled correctly
  - [ ] Validation errors returned clearly
- **Files:** `backend/src/services/job_search_service.py`

---

### 2.3 Job Search API
**Priority: P0 🔴 | Dependencies: BE-SVC-001**

#### BE-API-001: Job Search Endpoints
- **Priority:** P0 🔴
- **Effort:** 4 hours
- **Dependencies:** BE-SVC-001
- **Tasks:**
  1. Create router for job endpoints
  2. Implement POST /api/v1/jobs/search
  3. Implement GET /api/v1/jobs
  4. Implement GET /api/v1/jobs/{id}
  5. Implement POST /api/v1/jobs (manual entry)
  6. Add request/response models (Pydantic)
  7. Add pagination support
  8. Add filtering support
- **API Specifications:**
  ```python
  # backend/src/api/jobs.py

  @router.post("/jobs/search")
  async def search_jobs(
      request: JobSearchRequest,
      db: AsyncSession = Depends(get_db)
  ) -> JobSearchResponse

  @router.get("/jobs")
  async def list_jobs(
      skip: int = 0,
      limit: int = 20,
      filters: Optional[str] = None
  ) -> List[JobResponse]

  @router.get("/jobs/{job_id}")
  async def get_job(job_id: int) -> JobDetailResponse

  @router.post("/jobs")
  async def create_manual_job(request: CreateJobRequest) -> JobResponse
  ```
- **Acceptance Criteria:**
  - [ ] All endpoints return correct status codes
  - [ ] Request validation working (Pydantic)
  - [ ] Response models documented in OpenAPI
  - [ ] Pagination working correctly
  - [ ] Filters applied correctly
  - [ ] Error responses formatted consistently
- **Files:**
  - `backend/src/api/jobs.py`
  - `backend/src/api/schemas/job_schemas.py`
  - `backend/tests/test_api_jobs.py`

#### BE-API-002: Company Endpoints
- **Priority:** P2 🟡
- **Effort:** 2 hours
- **Dependencies:** BE-API-001
- **Tasks:**
  1. GET /api/v1/companies
  2. GET /api/v1/companies/{id}
  3. GET /api/v1/companies/{id}/jobs
- **Acceptance Criteria:**
  - [ ] Can list all companies
  - [ ] Can get company details
  - [ ] Can see all jobs for a company
- **Files:** `backend/src/api/companies.py`

---

### 2.4 Job Search Frontend
**Priority: P1 🟠 | Dependencies: BE-API-001**

#### FE-API-001: API Client Setup
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** BE-API-001
- **Tasks:**
  1. Create axios instance with config
  2. Create API client class
  3. Implement job search API calls
  4. Add error handling
  5. Add request/response interceptors
  6. Create React Query hooks
- **Implementation:**
  ```typescript
  // frontend/src/services/api.ts
  export const api = axios.create({
    baseURL: '/api/v1',
    timeout: 10000,
  })

  // frontend/src/services/jobsApi.ts
  export const jobsApi = {
    searchJobs: (params: JobSearchParams) => api.post('/jobs/search', params),
    getJob: (id: number) => api.get(`/jobs/${id}`),
    listJobs: (params: ListJobsParams) => api.get('/jobs', { params }),
    createJob: (data: CreateJobData) => api.post('/jobs', data),
  }

  // frontend/src/hooks/useJobs.ts
  export function useSearchJobs() {
    return useMutation({
      mutationFn: jobsApi.searchJobs,
    })
  }
  ```
- **Acceptance Criteria:**
  - [ ] All API calls working
  - [ ] Error handling displays user-friendly messages
  - [ ] Loading states managed
  - [ ] React Query caching configured
- **Files:**
  - `frontend/src/services/api.ts`
  - `frontend/src/services/jobsApi.ts`
  - `frontend/src/hooks/useJobs.ts`
  - `frontend/src/types/job.ts`

#### FE-UI-001: Job Components
- **Priority:** P1 🟠
- **Effort:** 5 hours
- **Dependencies:** FE-API-001
- **Tasks:**
  1. Create JobCard component
  2. Create JobList component
  3. Create JobFilters component
  4. Create SearchBar component
  5. Create JobDetail modal/page
  6. Add loading skeletons
  7. Add empty states
- **Components:**
  ```typescript
  // frontend/src/components/jobs/JobCard.tsx
  interface JobCardProps {
    job: Job
    onApply?: (job: Job) => void
    onSave?: (job: Job) => void
  }

  // frontend/src/components/jobs/JobList.tsx
  interface JobListProps {
    jobs: Job[]
    loading?: boolean
    onJobClick?: (job: Job) => void
  }

  // frontend/src/components/jobs/JobFilters.tsx
  interface JobFiltersProps {
    filters: JobFilters
    onChange: (filters: JobFilters) => void
  }
  ```
- **Acceptance Criteria:**
  - [ ] JobCard displays all key info (title, company, location, salary)
  - [ ] JobCard has save and apply actions
  - [ ] JobList handles empty states
  - [ ] JobFilters functional (remote, salary, type)
  - [ ] Components responsive (mobile-friendly)
  - [ ] Loading states pleasant
  - [ ] Dark mode working
- **Files:**
  - `frontend/src/components/jobs/JobCard.tsx`
  - `frontend/src/components/jobs/JobList.tsx`
  - `frontend/src/components/jobs/JobFilters.tsx`
  - `frontend/src/components/jobs/SearchBar.tsx`
  - `frontend/src/components/jobs/JobDetail.tsx`

#### FE-PAGE-001: Job Search Page
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** FE-UI-001
- **Tasks:**
  1. Replace JobsPage placeholder
  2. Integrate SearchBar component
  3. Integrate JobFilters component
  4. Integrate JobList component
  5. Add pagination
  6. Add sorting options
  7. Handle search state
  8. Add "Manual Entry" button
- **Implementation:**
  ```typescript
  // frontend/src/pages/JobsPage.tsx
  - Search bar at top
  - Filters sidebar (collapsible on mobile)
  - Job list in main area
  - Pagination at bottom
  - Floating "Add Manual Job" button
  ```
- **Acceptance Criteria:**
  - [ ] Search functionality working
  - [ ] Filters apply correctly
  - [ ] Results update in real-time
  - [ ] Pagination working
  - [ ] Can sort by date, relevance, salary
  - [ ] Manual entry opens modal/form
  - [ ] Mobile responsive
- **Files:** `frontend/src/pages/JobsPage.tsx`

#### FE-UI-002: Manual Job Entry Form
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** FE-API-001
- **Tasks:**
  1. Create ManualJobForm component
  2. Use react-hook-form + zod validation
  3. Add all job fields (title, company, URL required)
  4. Company autocomplete/creation
  5. Form submission handling
  6. Success/error feedback
- **Acceptance Criteria:**
  - [ ] Form validates required fields
  - [ ] Can create job with minimal data
  - [ ] Company autocomplete working
  - [ ] Success message on submit
  - [ ] Form resets after submit
- **Files:**
  - `frontend/src/components/jobs/ManualJobForm.tsx`
  - `frontend/src/schemas/jobSchema.ts`

---

### 2.5 Job Search Testing
**Priority: P1 🟠 | Dependencies: Above**

#### TEST-001: Backend Job Search Tests
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** BE-API-001, BE-SVC-001
- **Tasks:**
  1. Test JobSpy client (mocked)
  2. Test job search service
  3. Test normalization logic
  4. Test deduplication
  5. Test API endpoints
  6. Integration tests
- **Acceptance Criteria:**
  - [ ] Unit tests for all service methods
  - [ ] API endpoint tests (all status codes)
  - [ ] Edge cases covered
  - [ ] Coverage >80%
- **Files:**
  - `backend/tests/test_jobspy_client.py`
  - `backend/tests/test_job_search_service.py`
  - `backend/tests/test_api_jobs.py`

#### TEST-002: Frontend Job Search Tests
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** FE-PAGE-001
- **Tasks:**
  1. Test JobCard component
  2. Test JobList component
  3. Test JobFilters component
  4. Test SearchBar component
  5. Test JobsPage integration
- **Acceptance Criteria:**
  - [ ] Component renders correctly
  - [ ] User interactions work
  - [ ] API calls mocked
  - [ ] Coverage >75%
- **Files:**
  - `frontend/src/components/jobs/__tests__/`
  - `frontend/src/pages/__tests__/JobsPage.test.tsx`

---

## Phase 3: Application Tracking
**Timeline:** Week 5-6 | **Status:** After Phase 2

### 3.1 Application Backend
**Priority: P0 🔴 | Dependencies: Phase 2**

#### BE-SVC-003: Application Service
- **Priority:** P0 🔴
- **Effort:** 6 hours
- **Dependencies:** Phase 2 complete
- **Tasks:**
  1. Create ApplicationService class
  2. Implement CRUD operations
  3. Status update with history tracking
  4. Automatic status transitions
  5. Notification triggers
  6. Activity logging
- **Implementation:**
  ```python
  # backend/src/services/application_service.py
  class ApplicationService:
      async def create_application(job_id, user_id, data) -> Application
      async def update_application(app_id, data) -> Application
      async def update_status(app_id, new_status, notes) -> Application
      async def get_applications(filters) -> List[Application]
      async def get_application(app_id) -> Application
      async def delete_application(app_id) -> bool
      async def get_status_history(app_id) -> List[StatusHistory]
  ```
- **Acceptance Criteria:**
  - [ ] All CRUD operations working
  - [ ] Status changes recorded in history
  - [ ] Activity logs created automatically
  - [ ] Can filter by status, date, company
  - [ ] Includes related data (job, company)
- **Files:**
  - `backend/src/services/application_service.py`
  - `backend/tests/test_application_service.py`

#### BE-API-003: Application Endpoints
- **Priority:** P0 🔴
- **Effort:** 4 hours
- **Dependencies:** BE-SVC-003
- **Tasks:**
  1. POST /api/v1/applications
  2. GET /api/v1/applications
  3. GET /api/v1/applications/{id}
  4. PUT /api/v1/applications/{id}
  5. PATCH /api/v1/applications/{id}/status
  6. DELETE /api/v1/applications/{id}
  7. GET /api/v1/applications/{id}/history
- **Acceptance Criteria:**
  - [ ] All endpoints working
  - [ ] Proper validation
  - [ ] Status transitions validated
  - [ ] Pagination on list endpoint
  - [ ] Filtering working
- **Files:**
  - `backend/src/api/applications.py`
  - `backend/src/api/schemas/application_schemas.py`

---

### 3.2 Application Frontend
**Priority: P1 🟠 | Dependencies: BE-API-003**

#### FE-API-002: Application API Client
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-API-003
- **Tasks:**
  1. Create applications API client
  2. Create React Query hooks
  3. Add optimistic updates
- **Files:**
  - `frontend/src/services/applicationsApi.ts`
  - `frontend/src/hooks/useApplications.ts`

#### FE-UI-003: Application Components
- **Priority:** P1 🟠
- **Effort:** 6 hours
- **Dependencies:** FE-API-002
- **Tasks:**
  1. ApplicationCard component
  2. ApplicationList component
  3. ApplicationStatusBadge component
  4. StatusUpdateModal component
  5. ApplicationTimeline component
  6. ApplicationFilters component
- **Acceptance Criteria:**
  - [ ] Displays all application data
  - [ ] Status badge color-coded
  - [ ] Can update status inline
  - [ ] Timeline shows history
  - [ ] Mobile responsive
- **Files:**
  - `frontend/src/components/applications/`

#### FE-PAGE-002: Applications Page
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** FE-UI-003
- **Tasks:**
  1. Replace ApplicationsPage placeholder
  2. Kanban board view (optional)
  3. Table view
  4. Status filters
  5. Search functionality
  6. Bulk actions (optional)
- **Acceptance Criteria:**
  - [ ] Shows all applications
  - [ ] Can filter by status
  - [ ] Can search by company/title
  - [ ] Can update status quickly
  - [ ] Responsive layout
- **Files:** `frontend/src/pages/ApplicationsPage.tsx`

#### FE-PAGE-003: Application Detail Page
- **Priority:** P2 🟡
- **Effort:** 4 hours
- **Dependencies:** FE-UI-003
- **Tasks:**
  1. Create ApplicationDetailPage
  2. Show full job details
  3. Show application timeline
  4. Show notes section
  5. Show cover letters
  6. Edit application data
- **Files:** `frontend/src/pages/ApplicationDetailPage.tsx`

---

## Phase 4: LLM Integration & Cover Letters
**Timeline:** Week 7-8 | **Status:** After Phase 3

### 4.1 LLM Backend
**Priority: P1 🟠 | Dependencies: Phase 3**

#### BE-LLM-001: LLM Provider Interface
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** None
- **Tasks:**
  1. Create abstract LLMProvider class
  2. Define interface methods
  3. Create provider factory
- **Implementation:**
  ```python
  # backend/src/llm/provider.py
  class LLMProvider(ABC):
      @abstractmethod
      async def generate_text(prompt, **kwargs) -> str

      @abstractmethod
      async def generate_streaming(prompt, **kwargs) -> AsyncIterator[str]

  # backend/src/llm/factory.py
  def create_llm_provider(config) -> LLMProvider
  ```
- **Files:**
  - `backend/src/llm/provider.py`
  - `backend/src/llm/factory.py`

#### BE-LLM-002: Claude Integration
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** BE-LLM-001
- **Tasks:**
  1. Implement ClaudeProvider
  2. API key management
  3. Error handling
  4. Streaming support
  5. Token counting
- **Files:** `backend/src/llm/claude_provider.py`

#### BE-LLM-003: Ollama Integration
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** BE-LLM-001
- **Tasks:**
  1. Implement OllamaProvider
  2. Connection management
  3. Model selection
  4. Streaming support
- **Files:** `backend/src/llm/ollama_provider.py`

#### BE-SVC-004: Cover Letter Service
- **Priority:** P1 🟠
- **Effort:** 5 hours
- **Dependencies:** BE-LLM-002, BE-LLM-003
- **Tasks:**
  1. Create CoverLetterService
  2. Prompt templates (professional, casual, creative)
  3. Context building (job + profile)
  4. Generation method
  5. Save to database
  6. Version management
- **Implementation:**
  ```python
  class CoverLetterService:
      async def generate_cover_letter(
          job: Job,
          user_profile: str,
          style: str = "professional",
          provider: str = "claude"
      ) -> CoverLetter

      async def refine_cover_letter(
          cover_letter_id: int,
          feedback: str
      ) -> CoverLetter
  ```
- **Files:**
  - `backend/src/services/cover_letter_service.py`
  - `backend/src/llm/prompts.py`

#### BE-SVC-005: Job Analysis Service
- **Priority:** P2 🟡
- **Effort:** 4 hours
- **Dependencies:** BE-LLM-002, BE-LLM-003
- **Tasks:**
  1. Create JobAnalyzerService
  2. Extract required skills
  3. Extract preferred skills
  4. Determine experience level
  5. Extract salary info
  6. Calculate match score
- **Files:** `backend/src/services/job_analyzer_service.py`

#### BE-API-004: Cover Letter Endpoints
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** BE-SVC-004
- **Tasks:**
  1. POST /api/v1/cover-letters (generate)
  2. GET /api/v1/cover-letters/{id}
  3. PUT /api/v1/cover-letters/{id}
  4. GET /api/v1/applications/{id}/cover-letters
- **Files:** `backend/src/api/cover_letters.py`

#### BE-API-005: Job Analysis Endpoint
- **Priority:** P2 🟡
- **Effort:** 2 hours
- **Dependencies:** BE-SVC-005
- **Tasks:**
  1. POST /api/v1/jobs/{id}/analyze
- **Files:** `backend/src/api/jobs.py`

---

### 4.2 LLM Frontend
**Priority: P1 🟠 | Dependencies: BE-API-004**

#### FE-API-003: LLM API Client
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-API-004
- **Tasks:**
  1. Cover letter API client
  2. Job analysis API client
  3. React Query hooks
- **Files:**
  - `frontend/src/services/coverLettersApi.ts`
  - `frontend/src/hooks/useCoverLetters.ts`

#### FE-UI-004: Cover Letter Components
- **Priority:** P1 🟠
- **Effort:** 5 hours
- **Dependencies:** FE-API-003
- **Tasks:**
  1. CoverLetterGenerator component
  2. CoverLetterEditor component (markdown)
  3. CoverLetterPreview component
  4. StyleSelector component
  5. ProviderSelector (Claude/Ollama)
  6. Loading states with streaming
- **Files:** `frontend/src/components/coverLetters/`

#### FE-PAGE-004: Cover Letter Page
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** FE-UI-004
- **Tasks:**
  1. Create CoverLetterPage
  2. Job selection
  3. Profile input
  4. Style selection
  5. Generation + preview
  6. Edit and save
- **Files:** `frontend/src/pages/CoverLetterPage.tsx`

---

## Phase 5: MCP Server Implementation
**Timeline:** Week 9 | **Status:** After Phase 4

### 5.1 MCP Server Core
**Priority: P1 🟠 | Dependencies: Phase 4**

#### BE-MCP-001: MCP Server Foundation
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** Phase 4
- **Tasks:**
  1. Install FastMCP
  2. Create MCP server entry point
  3. Configure transport (stdio)
  4. Set up authentication
  5. Add logging
- **Files:**
  - `backend/src/mcp_server/server.py`
  - `backend/src/mcp_server/config.py`

#### BE-MCP-002: Tool - search_jobs
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement search_jobs tool
  2. Connect to JobSearchService
  3. Add Pydantic schemas
  4. Add error handling
- **Files:** `backend/src/mcp_server/tools/search_jobs.py`

#### BE-MCP-003: Tool - add_application
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement add_application tool
  2. Connect to ApplicationService
- **Files:** `backend/src/mcp_server/tools/add_application.py`

#### BE-MCP-004: Tool - generate_cover_letter
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement generate_cover_letter tool
  2. Connect to CoverLetterService
- **Files:** `backend/src/mcp_server/tools/generate_cover_letter.py`

#### BE-MCP-005: Tool - update_application_status
- **Priority:** P1 🟠
- **Effort:** 1 hour
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement update_application_status tool
  2. Connect to ApplicationService
- **Files:** `backend/src/mcp_server/tools/update_status.py`

#### BE-MCP-006: Tool - get_applications
- **Priority:** P1 🟠
- **Effort:** 1 hour
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement get_applications tool
  2. Support filters
- **Files:** `backend/src/mcp_server/tools/get_applications.py`

#### BE-MCP-007: Tool - analyze_job_requirements
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** BE-MCP-001
- **Tasks:**
  1. Implement analyze_job_requirements tool
  2. Connect to JobAnalyzerService
- **Files:** `backend/src/mcp_server/tools/analyze_job.py`

#### BE-MCP-008: MCP Resources
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** BE-MCP-002-007
- **Tasks:**
  1. Implement job:// resource
  2. Implement application:// resource
  3. Implement profile:// resource
  4. Implement stats:// resource
- **Files:** `backend/src/mcp_server/resources.py`

#### BE-MCP-009: MCP Prompts
- **Priority:** P2 🟡
- **Effort:** 2 hours
- **Dependencies:** BE-MCP-008
- **Tasks:**
  1. Implement job-search-assistant prompt
  2. Implement cover-letter-writer prompt
  3. Implement application-tracker prompt
- **Files:** `backend/src/mcp_server/prompts.py`

#### DOC-001: MCP Server Documentation
- **Priority:** P1 🟠
- **Effort:** 3 hours
- **Dependencies:** BE-MCP-009
- **Tasks:**
  1. Write MCP server setup guide
  2. Document all tools with examples
  3. Document all resources
  4. Document all prompts
  5. Claude Desktop integration guide
- **Files:** `docs/mcp-server-guide.md`

---

## Phase 6: Dashboard & Analytics
**Timeline:** Week 10 | **Status:** After Phase 5

### 6.1 Dashboard Backend
**Priority: P2 🟡 | Dependencies: Phase 3**

#### BE-SVC-006: Analytics Service
- **Priority:** P2 🟡
- **Effort:** 4 hours
- **Dependencies:** Phase 3
- **Tasks:**
  1. Create DashboardService
  2. Calculate statistics (total apps, by status, response rate)
  3. Timeline data (applications over time)
  4. Activity feed
  5. Trends analysis
- **Implementation:**
  ```python
  class DashboardService:
      async def get_statistics(user_id) -> DashboardStats
      async def get_timeline_data(user_id, days=30) -> TimelineData
      async def get_recent_activity(user_id, limit=20) -> List[Activity]
      async def get_application_funnel() -> FunnelData
  ```
- **Files:** `backend/src/services/dashboard_service.py`

#### BE-API-006: Dashboard Endpoints
- **Priority:** P2 🟡
- **Effort:** 2 hours
- **Dependencies:** BE-SVC-006
- **Tasks:**
  1. GET /api/v1/dashboard/stats
  2. GET /api/v1/dashboard/timeline
  3. GET /api/v1/dashboard/activity
- **Files:** `backend/src/api/dashboard.py`

#### BE-API-007: WebSocket for Real-time Updates
- **Priority:** P3 🟢
- **Effort:** 4 hours
- **Dependencies:** BE-SVC-006
- **Tasks:**
  1. Set up WebSocket endpoint
  2. Broadcast application updates
  3. Broadcast status changes
  4. Connection management
- **Files:** `backend/src/api/websocket.py`

---

### 6.2 Dashboard Frontend
**Priority: P2 🟡 | Dependencies: BE-API-006**

#### FE-API-004: Dashboard API Client
- **Priority:** P2 🟡
- **Effort:** 2 hours
- **Dependencies:** BE-API-006
- **Tasks:**
  1. Dashboard API client
  2. WebSocket client
  3. React Query hooks
- **Files:**
  - `frontend/src/services/dashboardApi.ts`
  - `frontend/src/services/websocket.ts`
  - `frontend/src/hooks/useDashboard.ts`

#### FE-UI-005: Dashboard Components
- **Priority:** P2 🟡
- **Effort:** 6 hours
- **Dependencies:** FE-API-004
- **Tasks:**
  1. StatCard component (total, active, interviews, offers)
  2. ApplicationChart component (Recharts)
  3. StatusPieChart component
  4. TimelineChart component
  5. ActivityFeed component
  6. QuickActions component
- **Files:** `frontend/src/components/dashboard/`

#### FE-PAGE-005: Dashboard Page
- **Priority:** P2 🟡
- **Effort:** 4 hours
- **Dependencies:** FE-UI-005
- **Tasks:**
  1. Replace DashboardPage placeholder
  2. Layout with stat cards
  3. Charts section
  4. Activity feed
  5. Quick actions
  6. Real-time updates via WebSocket
- **Files:** `frontend/src/pages/DashboardPage.tsx`

---

## Phase 7: Testing & Quality Assurance
**Timeline:** Week 11-12 | **Status:** Continuous + Final Polish

### 7.1 Backend Testing
**Priority: P1 🟠 | Dependencies: All backend features**

#### TEST-003: Complete Backend Test Suite
- **Priority:** P1 🟠
- **Effort:** 12 hours
- **Dependencies:** All backend code
- **Tasks:**
  1. Unit tests for all services (80%+ coverage)
  2. API endpoint tests (all routes)
  3. Integration tests (DB + API)
  4. MCP server tests
  5. LLM service tests (mocked)
  6. Error handling tests
  7. Performance tests
- **Acceptance Criteria:**
  - [ ] Backend coverage >80%
  - [ ] All endpoints tested
  - [ ] Edge cases covered
  - [ ] CI/CD passing
- **Files:** `backend/tests/`

#### QA-001: Backend Code Quality
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** All backend code
- **Tasks:**
  1. Run ruff on all code
  2. Run black formatter
  3. Run mypy type checker
  4. Fix all issues
  5. Add pre-commit hooks
- **Files:** `.pre-commit-config.yaml`

---

### 7.2 Frontend Testing
**Priority: P2 🟡 | Dependencies: All frontend features**

#### TEST-004: Complete Frontend Test Suite
- **Priority:** P2 🟡
- **Effort:** 10 hours
- **Dependencies:** All frontend code
- **Tasks:**
  1. Component tests (all components)
  2. Page tests (all pages)
  3. Hook tests (custom hooks)
  4. Integration tests (user flows)
  5. E2E tests (critical paths with Playwright)
- **Acceptance Criteria:**
  - [ ] Frontend coverage >75%
  - [ ] All components tested
  - [ ] User flows tested
- **Files:** `frontend/src/**/__tests__/`

#### QA-002: Frontend Code Quality
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** All frontend code
- **Tasks:**
  1. Run ESLint
  2. Run Prettier
  3. TypeScript strict check
  4. Fix all issues
  5. Add pre-commit hooks
- **Files:** `.pre-commit-config.yaml`

---

### 7.3 Security & Performance
**Priority: P1 🟠 | Dependencies: All code**

#### QA-003: Security Audit
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** All code
- **Tasks:**
  1. Check for hardcoded secrets
  2. SQL injection prevention review
  3. XSS prevention review
  4. CSRF protection
  5. Rate limiting verification
  6. Input validation audit
  7. Dependency vulnerability scan
- **Acceptance Criteria:**
  - [ ] No critical vulnerabilities
  - [ ] No secrets in code
  - [ ] All inputs validated
- **Files:** `docs/security-audit.md`

#### QA-004: Performance Testing
- **Priority:** P2 🟡
- **Effort:** 4 hours
- **Dependencies:** All code
- **Tasks:**
  1. Backend API load testing
  2. Database query optimization
  3. Frontend bundle size analysis
  4. Lighthouse audit
  5. Network request optimization
- **Acceptance Criteria:**
  - [ ] API responses < 500ms
  - [ ] Frontend bundle < 500KB
  - [ ] Lighthouse score >90
- **Files:** `docs/performance-report.md`

---

## Phase 8: Deployment & Polish
**Timeline:** Week 13 | **Status:** Final Phase

### 8.1 Deployment Infrastructure
**Priority: P0 🔴 | Dependencies: All code complete**

#### INFRA-001: Backend Docker Image
- **Priority:** P0 🔴
- **Effort:** 3 hours
- **Dependencies:** All backend code
- **Tasks:**
  1. Create production Dockerfile
  2. Multi-stage build optimization
  3. Security hardening
  4. Health checks
  5. Build and test image
- **Files:**
  - `backend/Dockerfile`
  - `backend/.dockerignore`

#### INFRA-002: Frontend Docker Image
- **Priority:** P0 🔴
- **Effort:** 2 hours
- **Dependencies:** All frontend code
- **Tasks:**
  1. Create production Dockerfile
  2. Nginx configuration
  3. Static file optimization
  4. Build and test image
- **Files:**
  - `frontend/Dockerfile`
  - `frontend/nginx.conf`

#### INFRA-003: Production Docker Compose
- **Priority:** P0 🔴
- **Effort:** 2 hours
- **Dependencies:** INFRA-001, INFRA-002
- **Tasks:**
  1. Update docker-compose.yml for production
  2. Add nginx reverse proxy (optional)
  3. Environment variable management
  4. Volume configuration
  5. Network configuration
- **Files:** `docker-compose.prod.yml`

#### INFRA-004: Database Backup Strategy
- **Priority:** P1 🟠
- **Effort:** 2 hours
- **Dependencies:** INFRA-003
- **Tasks:**
  1. Create backup script
  2. Restore script
  3. Schedule automation
  4. Test backup/restore
- **Files:** `scripts/backup_database.sh`

---

### 8.2 CI/CD Pipeline
**Priority: P2 🟡 | Dependencies: All code**

#### INFRA-005: GitHub Actions CI
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** TEST-003, TEST-004
- **Tasks:**
  1. Backend CI workflow (test, lint, build)
  2. Frontend CI workflow (test, lint, build)
  3. Docker image building
  4. Security scanning
- **Files:**
  - `.github/workflows/backend-ci.yml`
  - `.github/workflows/frontend-ci.yml`

#### INFRA-006: Deployment Automation
- **Priority:** P3 🟢
- **Effort:** 4 hours
- **Dependencies:** INFRA-005
- **Tasks:**
  1. Deploy to staging workflow
  2. Deploy to production workflow
  3. Rollback mechanism
- **Files:** `.github/workflows/deploy.yml`

---

### 8.3 Documentation
**Priority: P1 🟠 | Dependencies: All features**

#### DOC-002: User Documentation
- **Priority:** P1 🟠
- **Effort:** 6 hours
- **Dependencies:** All features
- **Tasks:**
  1. Complete README.md
  2. Installation guide
  3. Configuration guide
  4. User guide with screenshots
  5. FAQ section
  6. Troubleshooting guide
- **Files:**
  - `README.md`
  - `docs/user-guide.md`
  - `docs/installation.md`
  - `docs/troubleshooting.md`

#### DOC-003: API Documentation
- **Priority:** P1 🟠
- **Effort:** 4 hours
- **Dependencies:** All API endpoints
- **Tasks:**
  1. Review OpenAPI documentation
  2. Add examples to all endpoints
  3. Add authentication docs
  4. Export Postman collection
- **Files:** `docs/api-reference.md`

#### DOC-004: Architecture Documentation
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** All code
- **Tasks:**
  1. Update architecture diagrams
  2. Document all services
  3. Database schema documentation
  4. Deployment architecture
- **Files:** `docs/architecture.md`

#### DOC-005: Contributing Guide
- **Priority:** P3 🟢
- **Effort:** 2 hours
- **Dependencies:** All code
- **Tasks:**
  1. Contributing guidelines
  2. Code style guide
  3. Git workflow
  4. PR template
- **Files:**
  - `CONTRIBUTING.md`
  - `.github/PULL_REQUEST_TEMPLATE.md`

---

### 8.4 Final Polish
**Priority: P2 🟡 | Dependencies: All above**

#### QA-005: UI/UX Polish
- **Priority:** P2 🟡
- **Effort:** 6 hours
- **Dependencies:** All frontend code
- **Tasks:**
  1. Consistent spacing and alignment
  2. Loading states polish
  3. Error messages user-friendly
  4. Animations and transitions
  5. Accessibility audit (WCAG)
  6. Mobile optimization
- **Acceptance Criteria:**
  - [ ] No visual bugs
  - [ ] Consistent design language
  - [ ] Accessible (keyboard navigation, screen readers)
  - [ ] Mobile responsive

#### QA-006: Error Handling Audit
- **Priority:** P2 🟡
- **Effort:** 3 hours
- **Dependencies:** All code
- **Tasks:**
  1. Review all error cases
  2. Ensure user-friendly messages
  3. Proper logging
  4. Recovery mechanisms
- **Acceptance Criteria:**
  - [ ] No cryptic error messages
  - [ ] All errors logged properly
  - [ ] User can recover from errors

#### DOC-006: Demo Content
- **Priority:** P3 🟢
- **Effort:** 3 hours
- **Dependencies:** All features
- **Tasks:**
  1. Create demo video
  2. Take screenshots for README
  3. Create sample data
  4. Demo environment setup
- **Files:** `docs/demo/`

---

## Summary by Priority

### P0 Critical (Blocking) - Must Complete First
- BE-DB-001: Database migration
- BE-JOB-001: JobSpy integration
- BE-SVC-001: Job search service
- BE-API-001: Job search endpoints
- BE-SVC-003: Application service
- BE-API-003: Application endpoints
- INFRA-001-003: Docker images & compose

**Total P0 Tasks:** 10
**Estimated Effort:** ~30 hours

### P1 High (Essential for MVP) - Complete Next
- All remaining Phase 2-5 tasks
- Testing infrastructure
- Security audit
- User documentation

**Total P1 Tasks:** ~40
**Estimated Effort:** ~100 hours

### P2 Medium (Important) - After MVP
- Dashboard and analytics
- Frontend testing
- Performance optimization
- Advanced features

**Total P2 Tasks:** ~25
**Estimated Effort:** ~60 hours

### P3 Low (Nice-to-have) - Polish Phase
- CI/CD automation
- Contributing guides
- Demo content
- Advanced deployment

**Total P3 Tasks:** ~10
**Estimated Effort:** ~20 hours

---

## Quick Reference: Next 10 Tasks

1. **BE-DB-001** 🔴 - Create database migration (1 hour)
2. **BE-JOB-001** 🔴 - JobSpy integration (4 hours)
3. **BE-SVC-001** 🔴 - Job search service (6 hours)
4. **BE-API-001** 🔴 - Job search endpoints (4 hours)
5. **FE-API-001** 🟠 - API client setup (3 hours)
6. **FE-UI-001** 🟠 - Job components (5 hours)
7. **FE-PAGE-001** 🟠 - Job search page (4 hours)
8. **TEST-001** 🟠 - Backend job tests (4 hours)
9. **BE-SVC-003** 🔴 - Application service (6 hours)
10. **BE-API-003** 🔴 - Application endpoints (4 hours)

**Total for next 10 tasks:** ~41 hours (~1 week of focused work)

---

## Progress Tracking

Update this section as tasks complete:

- **Phase 1:** ✅ Complete (Week 1)
- **Phase 2:** ⏳ Next (Week 2-4)
- **Phase 3:** 📋 Planned (Week 5-6)
- **Phase 4:** 📋 Planned (Week 7-8)
- **Phase 5:** 📋 Planned (Week 9)
- **Phase 6:** 📋 Planned (Week 10)
- **Phase 7:** 📋 Planned (Week 11-12)
- **Phase 8:** 📋 Planned (Week 13)

**Last Updated:** November 22, 2025
