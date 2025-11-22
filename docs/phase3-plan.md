# Phase 3 Implementation Plan - Application Tracking

**Phase:** 3 - Application Tracking
**Timeline:** Estimated 8-12 hours (1-2 sessions)
**Dependencies:** Phase 2 Complete ✅
**Status:** Ready to Start
**Priority:** P0 🔴 (Core Functionality)

---

## 📊 Executive Summary

Phase 3 adds **application tracking** functionality to Job-o-matic, enabling users to:
- Create applications from job listings
- Track application status through pipeline stages
- View application history and timeline
- Add notes and reminders
- Filter and search applications
- Manage application lifecycle (draft → submitted → interview → offer/rejected)

**Estimated Deliverable:** 2,000+ lines of code across 12+ files

---

## 🎯 Goals

### Primary Goals
1. ✅ Complete backend application management system
2. ✅ Build frontend application tracking UI
3. ✅ Implement status tracking with history
4. ✅ Create intuitive application dashboard

### Success Metrics
- Can create application from any job listing
- Can update application status with one click
- Can view full application timeline
- Can filter applications by status, company, date
- All operations < 500ms response time

---

## 📋 Task Breakdown

### Phase 3.1: Application Backend (6 tasks)

#### BE-SVC-003: Application Service
**Priority:** P0 🔴 | **Effort:** 6 hours | **Dependencies:** Phase 2

**Location:** `backend/src/services/application_service.py` (~600 lines)

**Tasks:**
1. ✅ Create ApplicationService class with dependency injection
2. ✅ Implement CRUD operations
   - create_application(job_id, user_id, data) → Application
   - get_applications(filters) → List[Application]
   - get_application(app_id) → Application
   - update_application(app_id, data) → Application
   - delete_application(app_id) → bool
3. ✅ Implement status management
   - update_status(app_id, new_status, notes) → Application
   - validate_status_transition(current, new) → bool
   - get_status_history(app_id) → List[StatusHistory]
4. ✅ Implement history tracking
   - Auto-create StatusHistory on status change
   - Record timestamp, old/new status, notes
5. ✅ Implement activity logging
   - Log all create/update/delete operations
   - Include user_id, action, metadata
6. ✅ Add filtering and search
   - Filter by: status, company_id, date_range, is_active
   - Search by: job title, company name
7. ✅ Add statistics helpers
   - get_application_stats(user_id) → dict (counts by status)
   - get_recent_activity(user_id, limit) → List[Activity]

**Implementation Pattern:**
```python
class ApplicationService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_application(
        self,
        job_id: int,
        user_id: int,
        status: ApplicationStatus = ApplicationStatus.DRAFT,
        notes: Optional[str] = None,
        **kwargs
    ) -> Application:
        # Verify job exists
        # Create application
        # Log activity
        # Return created application

    async def update_status(
        self,
        app_id: int,
        new_status: ApplicationStatus,
        notes: Optional[str] = None,
    ) -> Application:
        # Get current application
        # Validate status transition
        # Create status history entry
        # Update application
        # Log activity
        # Return updated application
```

**Acceptance Criteria:**
- [ ] All CRUD operations working correctly
- [ ] Status changes recorded in application_status_history table
- [ ] Activity logs created automatically for all operations
- [ ] Can filter applications by status, company, date range
- [ ] Includes eager-loaded relationships (job, company)
- [ ] Proper error handling for invalid transitions
- [ ] All async/await properly used

---

#### BE-API-003: Application API Endpoints
**Priority:** P0 🔴 | **Effort:** 4 hours | **Dependencies:** BE-SVC-003

**Files:**
- `backend/src/api/applications.py` (~400 lines)
- `backend/src/api/schemas/application_schemas.py` (~250 lines)

**Endpoints (7 total):**

1. **POST /api/v1/applications** - Create application
   - Request: CreateApplicationRequest
   - Response: ApplicationDetailResponse (201)
   - Auth: Required

2. **GET /api/v1/applications** - List applications
   - Query Params: status, company_id, skip, limit, is_active
   - Response: List[ApplicationResponse] (200)
   - Pagination: skip/limit
   - Auth: Required

3. **GET /api/v1/applications/{id}** - Get application details
   - Path Param: application_id
   - Response: ApplicationDetailResponse (200)
   - Includes: job, company, status_history
   - Auth: Required

4. **PUT /api/v1/applications/{id}** - Update application
   - Request: UpdateApplicationRequest
   - Response: ApplicationDetailResponse (200)
   - Auth: Required

5. **PATCH /api/v1/applications/{id}/status** - Update status
   - Request: UpdateStatusRequest {status, notes}
   - Response: ApplicationDetailResponse (200)
   - Auth: Required

6. **DELETE /api/v1/applications/{id}** - Delete application
   - Response: 204 No Content
   - Soft delete (sets is_active = False)
   - Auth: Required

7. **GET /api/v1/applications/{id}/history** - Get status history
   - Response: List[StatusHistoryResponse] (200)
   - Ordered by created_at DESC
   - Auth: Required

**Pydantic Schemas:**
```python
# Request Schemas
class CreateApplicationRequest(BaseModel):
    job_id: int
    status: ApplicationStatus = ApplicationStatus.DRAFT
    notes: Optional[str] = None
    resume_version: Optional[str] = None
    cover_letter_id: Optional[int] = None

class UpdateApplicationRequest(BaseModel):
    status: Optional[ApplicationStatus] = None
    notes: Optional[str] = None
    resume_version: Optional[str] = None
    interview_date: Optional[datetime] = None

class UpdateStatusRequest(BaseModel):
    status: ApplicationStatus
    notes: Optional[str] = None

# Response Schemas
class ApplicationResponse(BaseModel):
    id: int
    job: JobResponse
    status: ApplicationStatus
    applied_date: Optional[datetime]
    created_at: datetime
    updated_at: datetime

class ApplicationDetailResponse(ApplicationResponse):
    notes: Optional[str]
    resume_version: Optional[str]
    interview_date: Optional[datetime]
    offer_deadline: Optional[datetime]
    status_history: List[StatusHistoryResponse]

class StatusHistoryResponse(BaseModel):
    id: int
    old_status: ApplicationStatus
    new_status: ApplicationStatus
    notes: Optional[str]
    created_at: datetime
```

**Acceptance Criteria:**
- [ ] All 7 endpoints working correctly
- [ ] Proper HTTP status codes (200, 201, 204, 404, 422)
- [ ] Pydantic validation on all requests
- [ ] OpenAPI documentation auto-generated
- [ ] Eager loading relationships (no N+1 queries)
- [ ] Error messages user-friendly
- [ ] Status transitions validated

---

### Phase 3.2: Application Frontend (4 tasks)

#### FE-API-002: Application API Client & Hooks
**Priority:** P1 🟠 | **Effort:** 2 hours | **Dependencies:** BE-API-003

**Files:**
- `frontend/src/api/applications.api.ts` (~100 lines)
- `frontend/src/hooks/useApplications.ts` (~200 lines)
- `frontend/src/types/application.types.ts` (~120 lines)

**TypeScript Types:**
```typescript
export enum ApplicationStatus {
  DRAFT = 'draft',
  SUBMITTED = 'submitted',
  SCREENING = 'screening',
  INTERVIEW = 'interview',
  TECHNICAL = 'technical',
  OFFER = 'offer',
  ACCEPTED = 'accepted',
  REJECTED = 'rejected',
  WITHDRAWN = 'withdrawn',
}

export interface Application {
  id: number
  job: Job
  status: ApplicationStatus
  applied_date?: string
  notes?: string
  created_at: string
  updated_at: string
}

export interface ApplicationDetail extends Application {
  resume_version?: string
  interview_date?: string
  offer_deadline?: string
  status_history: StatusHistory[]
}

export interface StatusHistory {
  id: number
  old_status: ApplicationStatus
  new_status: ApplicationStatus
  notes?: string
  created_at: string
}
```

**API Client Methods:**
- createApplication(request)
- listApplications(params)
- getApplication(id)
- updateApplication(id, request)
- updateStatus(id, status, notes)
- deleteApplication(id)
- getStatusHistory(id)

**React Query Hooks:**
- useApplicationList(params)
- useApplication(id)
- useCreateApplication()
- useUpdateApplication()
- useUpdateStatus()
- useDeleteApplication()

**Acceptance Criteria:**
- [ ] Full TypeScript type coverage
- [ ] React Query caching (2min TTL)
- [ ] Optimistic updates for status changes
- [ ] Proper error handling
- [ ] Cache invalidation on mutations

---

#### FE-UI-003: Application UI Components
**Priority:** P1 🟠 | **Effort:** 6 hours | **Dependencies:** FE-API-002

**Components (6 total):**

1. **ApplicationCard.tsx** (~180 lines)
   - Displays single application in card format
   - Shows: job title, company, status badge, dates
   - Actions: quick status update, view details, delete
   - Props: application, onStatusUpdate, onDelete, onClick

2. **ApplicationList.tsx** (~120 lines)
   - Renders list of ApplicationCard components
   - Loading/error/empty states
   - Props: applications, loading, error, onApplicationClick

3. **ApplicationStatusBadge.tsx** (~80 lines)
   - Color-coded status badge
   - Status-specific icons
   - Props: status, size ('sm' | 'md' | 'lg')
   - Colors:
     - draft: gray
     - submitted: blue
     - screening: yellow
     - interview: purple
     - technical: indigo
     - offer: green
     - accepted: emerald
     - rejected: red
     - withdrawn: gray

4. **StatusUpdateModal.tsx** (~200 lines)
   - Modal for updating application status
   - Dropdown for new status
   - Optional notes textarea
   - Validation: prevent invalid transitions
   - Props: application, isOpen, onClose, onUpdate

5. **ApplicationTimeline.tsx** (~150 lines)
   - Vertical timeline of status history
   - Shows: date, old→new status, notes
   - Props: statusHistory

6. **ApplicationFilters.tsx** (~180 lines)
   - Filter panel (collapsible)
   - Filters: status (multi-select), date range, company
   - Props: onFilterChange, onReset

**Acceptance Criteria:**
- [ ] All components render correctly
- [ ] Dark mode support
- [ ] Mobile responsive
- [ ] Proper loading states
- [ ] Error handling
- [ ] Accessible (keyboard navigation, ARIA labels)

---

#### FE-PAGE-003: Applications Page
**Priority:** P1 🟠 | **Effort:** 4 hours | **Dependencies:** FE-UI-003

**File:** `frontend/src/pages/ApplicationsPage.tsx` (~250 lines)

**Features:**
1. **Header Section**
   - Page title
   - Statistics (counts by status)
   - "Add Application" button

2. **Filters Section**
   - Status filter (dropdown or tabs)
   - Search bar (job title, company)
   - Filter button (opens ApplicationFilters)

3. **Main Content**
   - Grid/List view of ApplicationCard components
   - Empty state: "No applications yet - search for jobs and apply!"
   - Loading state: skeleton cards
   - Error state: error message with retry

4. **Status Tabs (optional enhanced UX)**
   - All | Draft | Submitted | Interview | Offer | Rejected
   - Show count for each status
   - Click to filter

**Layout:**
```
┌─────────────────────────────────────┐
│ Applications          [Add +]       │
│ 3 Active • 2 Interview • 1 Offer    │
├─────────────────────────────────────┤
│ [All] [Draft] [Submitted] [Inter...│
│ [Search]         [Filters ▼]        │
├─────────────────────────────────────┤
│ ┌──────────────┐ ┌──────────────┐  │
│ │ App Card 1   │ │ App Card 2   │  │
│ └──────────────┘ └──────────────┘  │
│ ┌──────────────┐ ┌──────────────┐  │
│ │ App Card 3   │ │ App Card 4   │  │
│ └──────────────┘ └──────────────┘  │
└─────────────────────────────────────┘
```

**Acceptance Criteria:**
- [ ] Shows all user applications
- [ ] Can filter by status
- [ ] Can search by job title/company
- [ ] Can update status quickly (one-click)
- [ ] Can delete applications
- [ ] Shows statistics
- [ ] Responsive layout

---

#### FE-PAGE-004: Application Detail Page (Optional - P2)
**Priority:** P2 🟡 | **Effort:** 4 hours | **Dependencies:** FE-UI-003

**File:** `frontend/src/pages/ApplicationDetailPage.tsx` (~300 lines)

**Route:** `/applications/:id`

**Sections:**
1. Header: Job info, company, status badge
2. Actions: Update status, edit application, delete
3. Application Details: notes, dates, resume version
4. Status Timeline: ApplicationTimeline component
5. Related Job: Link to original job listing
6. Cover Letters: List of associated cover letters (Phase 4)

**Note:** This is marked P2 as the ApplicationsPage provides core functionality. Detail page adds polish.

---

## 📊 Code Metrics Estimate

| Component | Files | Lines | Complexity |
|-----------|-------|-------|------------|
| **Backend Service** | 1 | 600 | High |
| **Backend API** | 2 | 650 | Medium |
| **Backend Tests** | 2 | 400 | Medium |
| **Frontend Types** | 1 | 120 | Low |
| **Frontend API** | 2 | 300 | Low |
| **Frontend Components** | 6 | 910 | Medium |
| **Frontend Pages** | 1 | 250 | Medium |
| **Total** | **15** | **~3,230** | - |

---

## 🔄 Integration Points

### With Phase 2 (Jobs)
- Create application from job listing (job_id reference)
- Display job details in ApplicationCard
- Link from job to applications

### With Phase 4 (LLM/Cover Letters)
- Associate cover letters with applications
- Generate cover letters when creating application
- Display cover letter in application detail

### With Phase 6 (Dashboard)
- Application statistics for dashboard
- Recent activity feed
- Application status distribution chart

---

## 🧪 Testing Strategy

### Backend Tests
1. **Unit Tests** - ApplicationService
   - Test all CRUD operations
   - Test status transition validation
   - Test history creation
   - Test activity logging
   - Test filtering logic

2. **API Tests** - Application Endpoints
   - Test all endpoints
   - Test validation (422 responses)
   - Test error handling (404, 500)
   - Test authentication (when implemented)

3. **Integration Tests**
   - Test full create → update → delete flow
   - Test status lifecycle
   - Test relationships (job, company loading)

### Frontend Tests (Optional for Phase 3)
- Component tests with React Testing Library
- Hook tests with @testing-library/react-hooks
- E2E tests with Playwright (defer to Phase 7)

---

## 📝 Implementation Order

### Session 1: Backend (4-6 hours)
1. ✅ BE-SVC-003: ApplicationService (~3 hours)
   - Core CRUD operations
   - Status management
   - History tracking
   - Filtering

2. ✅ BE-API-003: Application Endpoints (~2 hours)
   - All 7 REST endpoints
   - Pydantic schemas
   - OpenAPI docs

3. ✅ Update main.py - Include application router

4. ✅ Test with cURL/Postman - Manual testing

5. ⏳ Write unit tests (optional - can defer)

### Session 2: Frontend (4-6 hours)
1. ✅ FE-API-002: Types, API Client, Hooks (~2 hours)
   - TypeScript types
   - Axios API methods
   - React Query hooks

2. ✅ FE-UI-003: Components (~3 hours)
   - ApplicationCard
   - ApplicationList
   - ApplicationStatusBadge
   - StatusUpdateModal
   - ApplicationTimeline
   - ApplicationFilters

3. ✅ FE-PAGE-003: ApplicationsPage (~1.5 hours)
   - Layout
   - Integration
   - Filters
   - Statistics

4. ✅ Update App.tsx routes - Add /applications/:id route (if detail page)

---

## ⚠️ Known Challenges & Solutions

### Challenge 1: Status Transition Validation
**Problem:** Need to prevent invalid status transitions (e.g., can't go from REJECTED back to DRAFT)

**Solution:**
- Define valid transitions in ApplicationService
- Validate before updating
- Return clear error messages

```python
VALID_TRANSITIONS = {
    ApplicationStatus.DRAFT: [ApplicationStatus.SUBMITTED, ApplicationStatus.WITHDRAWN],
    ApplicationStatus.SUBMITTED: [ApplicationStatus.SCREENING, ApplicationStatus.REJECTED],
    ApplicationStatus.SCREENING: [ApplicationStatus.INTERVIEW, ApplicationStatus.REJECTED],
    # ... etc
}
```

### Challenge 2: Eager Loading Relationships
**Problem:** N+1 query problem when loading applications with jobs and companies

**Solution:**
- Use `selectinload` for all queries
- Example: `select(Application).options(selectinload(Application.job).selectinload(Job.company))`

### Challenge 3: Optimistic UI Updates
**Problem:** UI feels slow waiting for status update API call

**Solution:**
- Use React Query's `onMutate` for optimistic updates
- Rollback on error
- Show success/error toasts

---

## 🎯 Success Criteria

### Functional Requirements
- [ ] Can create application from any job
- [ ] Can view all applications
- [ ] Can update application status
- [ ] Can view status history timeline
- [ ] Can filter applications by status
- [ ] Can search applications
- [ ] Can delete applications
- [ ] Status changes are logged

### Non-Functional Requirements
- [ ] API responses < 500ms
- [ ] UI is responsive (mobile + desktop)
- [ ] No N+1 query problems
- [ ] Proper error handling throughout
- [ ] Type-safe (TypeScript + Pydantic)
- [ ] Dark mode supported
- [ ] Code is documented

---

## 📅 Timeline

| Task | Duration | Dependencies |
|------|----------|--------------|
| BE-SVC-003 | 3 hours | Phase 2 ✅ |
| BE-API-003 | 2 hours | BE-SVC-003 |
| BE Tests | 2 hours | BE-API-003 |
| FE-API-002 | 2 hours | BE-API-003 |
| FE-UI-003 | 3 hours | FE-API-002 |
| FE-PAGE-003 | 1.5 hours | FE-UI-003 |
| **Total** | **13.5 hours** | - |

**Buffer:** +2 hours for bugs/polish = **~16 hours** total

**Sessions:** 2 sessions of 6-8 hours each

---

## 🚀 Next Steps After Phase 3

1. **Phase 4: LLM Integration** - Cover letter generation
2. **Phase 5: MCP Server** - Claude integration
3. **Phase 6: Dashboard** - Analytics and insights
4. **Phase 7: Testing** - Comprehensive test suite
5. **Phase 8: Deployment** - Production setup

---

## 🎉 Phase 3 Deliverables

1. ✅ Complete backend application tracking system
2. ✅ Full REST API with 7 endpoints
3. ✅ React frontend with application management
4. ✅ Status tracking with history
5. ✅ Filtering and search
6. ✅ Responsive UI components
7. ✅ OpenAPI documentation

**Estimated Total:** 3,230 lines of code, 15 files

---

**Phase 3: Ready to Begin! 🚀**
