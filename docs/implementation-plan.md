# Job-o-matic Implementation Plan

**Version:** 1.0
**Date:** November 22, 2025
**Status:** Phase 1 Research Complete - Awaiting Approval

## Project Overview

**Goal:** Build an enterprise-grade job application management system with MCP integration, AI-powered cover letters, and comprehensive tracking capabilities.

**Timeline:** 8-10 weeks for full implementation
**Team Size:** 1-2 developers
**Deployment Target:** Docker containers (local + cloud-ready)

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Interface                          │
│                  (React Dashboard - Port 5173)                  │
└────────────────────────────────┬────────────────────────────────┘
                                 │
                                 │ HTTP/WebSocket
                                 ▼
┌─────────────────────────────────────────────────────────────────┐
│                      FastAPI Backend                            │
│                       (Port 8000)                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  REST API    │  │  WebSocket   │  │  MCP Server  │         │
│  │  Endpoints   │  │  Real-time   │  │  (FastMCP)   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└───────────┬──────────────┬─────────────────┬──────────────────┘
            │              │                 │
            ▼              ▼                 ▼
┌──────────────────┐ ┌──────────┐ ┌─────────────────┐
│   PostgreSQL     │ │   LLM    │ │  Job Search     │
│   Database       │ │ Services │ │  Engine         │
│                  │ │          │ │                 │
│ ┌──────────────┐ │ │ ┌──────┐ │ │ ┌─────────────┐ │
│ │ Jobs         │ │ │ │Claude│ │ │ │  JobSpy API │ │
│ │ Applications │ │ │ └──────┘ │ │ └─────────────┘ │
│ │ CoverLetters │ │ │ ┌──────┐ │ │ ┌─────────────┐ │
│ │ Companies    │ │ │ │Ollama│ │ │ │  Playwright │ │
│ │ Users        │ │ │ └──────┘ │ │ │  (Selective)│ │
│ └──────────────┘ │ │          │ │ └─────────────┘ │
└──────────────────┘ └──────────┘ └─────────────────┘
```

### MCP Integration Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                     Claude Desktop                           │
│                    (MCP Client)                              │
└────────────────────────────┬─────────────────────────────────┘
                             │
                             │ MCP Protocol (stdio/HTTP)
                             ▼
┌──────────────────────────────────────────────────────────────┐
│                  Job-o-matic MCP Server                      │
│                      (FastMCP)                               │
│                                                              │
│  ┌────────────────────────────────────────────────────┐     │
│  │                    Tools                           │     │
│  │  • search_jobs()                                   │     │
│  │  • add_application()                               │     │
│  │  • generate_cover_letter()                         │     │
│  │  • update_application_status()                     │     │
│  │  • get_applications()                              │     │
│  │  • analyze_job_requirements()                      │     │
│  └────────────────────────────────────────────────────┘     │
│                                                              │
│  ┌────────────────────────────────────────────────────┐     │
│  │                  Resources                         │     │
│  │  • job://{job_id}                                  │     │
│  │  • application://{app_id}                          │     │
│  │  • profile://user                                  │     │
│  │  • stats://dashboard                               │     │
│  └────────────────────────────────────────────────────┘     │
│                                                              │
│  ┌────────────────────────────────────────────────────┐     │
│  │                   Prompts                          │     │
│  │  • /job-search-assistant                           │     │
│  │  • /cover-letter-writer                            │     │
│  │  • /application-tracker                            │     │
│  └────────────────────────────────────────────────────┘     │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│              Business Logic Layer                            │
│  (JobService, ApplicationService, LLMService, etc.)          │
└───────────────────────────┬──────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                   PostgreSQL Database                        │
└──────────────────────────────────────────────────────────────┘
```

### Component Interaction Flow

```
┌─────────┐
│  User   │
└────┬────┘
     │
     │ (1) Search for "Python Developer" in "San Francisco"
     ▼
┌─────────────────┐
│ React Dashboard │
└────┬────────────┘
     │
     │ (2) POST /api/jobs/search
     ▼
┌──────────────────┐
│  FastAPI Router  │
└────┬─────────────┘
     │
     │ (3) Call JobSearchService.search()
     ▼
┌─────────────────────┐
│  Job Search Engine  │
│  ┌───────────────┐  │
│  │ Try JobSpy API│  │
│  └───────┬───────┘  │
│          │          │
│          │ (4) External API call
│          ▼          │
│  ┌───────────────┐  │
│  │ Normalize Data│  │
│  └───────┬───────┘  │
│          │          │
│          │ (5) Deduplicate
│          ▼          │
│  ┌───────────────┐  │
│  │  Return Jobs  │  │
│  └───────────────┘  │
└────┬────────────────┘
     │
     │ (6) Save to DB + return results
     ▼
┌──────────────────┐
│  PostgreSQL DB   │
└──────────────────┘
     │
     │ (7) Return JSON to frontend
     ▼
┌─────────────────┐
│ React Dashboard │ → Display job cards
└─────────────────┘
```

## Database Schema Design

### Entity Relationship Diagram

```
┌─────────────────┐         ┌──────────────────┐
│     Users       │         │    Companies     │
├─────────────────┤         ├──────────────────┤
│ id (PK)         │         │ id (PK)          │
│ email           │         │ name             │
│ name            │         │ website          │
│ resume_text     │         │ description      │
│ skills[]        │         │ industry         │
│ created_at      │         │ logo_url         │
│ updated_at      │         │ created_at       │
└────────┬────────┘         └────────┬─────────┘
         │                           │
         │                           │
         │    ┌──────────────────────┼───────────┐
         │    │                      │           │
         ▼    ▼                      ▼           │
┌─────────────────────┐      ┌──────────────────┐
│       Jobs          │      │   Applications   │
├─────────────────────┤      ├──────────────────┤
│ id (PK)             │◄─────│ id (PK)          │
│ company_id (FK)     │      │ job_id (FK)      │
│ title               │      │ user_id (FK)     │
│ description         │      │ status           │
│ location            │      │ applied_date     │
│ remote_policy       │      │ notes            │
│ salary_min          │      │ resume_version   │
│ salary_max          │      │ created_at       │
│ employment_type     │      │ updated_at       │
│ source              │      └────────┬─────────┘
│ url                 │               │
│ posted_date         │               │
│ requirements_parsed │               │
│ created_at          │               ▼
│ updated_at          │      ┌──────────────────┐
└─────────────────────┘      │  CoverLetters    │
         │                   ├──────────────────┤
         │                   │ id (PK)          │
         │                   │ application_id(FK)│
         │                   │ content          │
         │                   │ version          │
         │                   │ llm_provider     │
         │                   │ created_at       │
         └───────────────────┤ updated_at       │
                             └──────────────────┘

┌──────────────────┐         ┌──────────────────┐
│  SearchQueries   │         │  ActivityLog     │
├──────────────────┤         ├──────────────────┤
│ id (PK)          │         │ id (PK)          │
│ user_id (FK)     │         │ user_id (FK)     │
│ query            │         │ action_type      │
│ location         │         │ entity_type      │
│ filters          │         │ entity_id        │
│ results_count    │         │ details          │
│ created_at       │         │ created_at       │
└──────────────────┘         └──────────────────┘
```

### SQLAlchemy Models

```python
# backend/src/models/database.py

from datetime import datetime
from typing import Optional, List
from sqlalchemy import String, Text, Integer, DateTime, Enum, ARRAY, JSON, ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
import enum

class Base(DeclarativeBase):
    pass

class ApplicationStatus(str, enum.Enum):
    INTERESTED = "interested"
    APPLIED = "applied"
    SCREENING = "screening"
    INTERVIEW = "interview"
    OFFER = "offer"
    REJECTED = "rejected"
    ACCEPTED = "accepted"
    WITHDRAWN = "withdrawn"

class RemotePolicy(str, enum.Enum):
    REMOTE = "remote"
    HYBRID = "hybrid"
    ONSITE = "onsite"
    UNKNOWN = "unknown"

class EmploymentType(str, enum.Enum):
    FULL_TIME = "full_time"
    PART_TIME = "part_time"
    CONTRACT = "contract"
    TEMPORARY = "temporary"
    INTERNSHIP = "internship"

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    resume_text: Mapped[Optional[str]] = mapped_column(Text)
    skills: Mapped[List[str]] = mapped_column(ARRAY(String), default=[])
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    applications: Mapped[List["Application"]] = relationship(back_populates="user")
    search_queries: Mapped[List["SearchQuery"]] = relationship(back_populates="user")
    activity_logs: Mapped[List["ActivityLog"]] = relationship(back_populates="user")

class Company(Base):
    __tablename__ = "companies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), index=True)
    website: Mapped[Optional[str]] = mapped_column(String(500))
    description: Mapped[Optional[str]] = mapped_column(Text)
    industry: Mapped[Optional[str]] = mapped_column(String(100))
    logo_url: Mapped[Optional[str]] = mapped_column(String(500))
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    jobs: Mapped[List["Job"]] = relationship(back_populates="company")

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(primary_key=True)
    company_id: Mapped[int] = mapped_column(ForeignKey("companies.id"))
    title: Mapped[str] = mapped_column(String(255), index=True)
    description: Mapped[str] = mapped_column(Text)
    location: Mapped[str] = mapped_column(String(255))
    remote_policy: Mapped[RemotePolicy] = mapped_column(Enum(RemotePolicy), default=RemotePolicy.UNKNOWN)
    salary_min: Mapped[Optional[int]] = mapped_column(Integer)
    salary_max: Mapped[Optional[int]] = mapped_column(Integer)
    employment_type: Mapped[EmploymentType] = mapped_column(Enum(EmploymentType))
    source: Mapped[str] = mapped_column(String(50))  # "jobspy", "scraped", "manual"
    url: Mapped[str] = mapped_column(String(1000))
    posted_date: Mapped[Optional[datetime]] = mapped_column(DateTime)

    # Parsed requirements (from LLM analysis)
    requirements_parsed: Mapped[Optional[dict]] = mapped_column(JSON)
    # Structure: {
    #   "required_skills": ["Python", "FastAPI"],
    #   "preferred_skills": ["Docker", "AWS"],
    #   "experience_years": "3-5",
    #   "education": "Bachelor's in CS",
    #   "match_score": 85
    # }

    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    company: Mapped["Company"] = relationship(back_populates="jobs")
    applications: Mapped[List["Application"]] = relationship(back_populates="job")

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(primary_key=True)
    job_id: Mapped[int] = mapped_column(ForeignKey("jobs.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    status: Mapped[ApplicationStatus] = mapped_column(Enum(ApplicationStatus), default=ApplicationStatus.INTERESTED)
    applied_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    notes: Mapped[Optional[str]] = mapped_column(Text)
    resume_version: Mapped[Optional[str]] = mapped_column(String(100))  # e.g., "v2_tech_focus"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    job: Mapped["Job"] = relationship(back_populates="applications")
    user: Mapped["User"] = relationship(back_populates="applications")
    cover_letters: Mapped[List["CoverLetter"]] = relationship(back_populates="application")

class CoverLetter(Base):
    __tablename__ = "cover_letters"

    id: Mapped[int] = mapped_column(primary_key=True)
    application_id: Mapped[int] = mapped_column(ForeignKey("applications.id"))
    content: Mapped[str] = mapped_column(Text)
    version: Mapped[int] = mapped_column(Integer, default=1)
    llm_provider: Mapped[str] = mapped_column(String(50))  # "claude", "ollama"
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    application: Mapped["Application"] = relationship(back_populates="cover_letters")

class SearchQuery(Base):
    __tablename__ = "search_queries"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    query: Mapped[str] = mapped_column(String(500))
    location: Mapped[str] = mapped_column(String(255))
    filters: Mapped[Optional[dict]] = mapped_column(JSON)  # {"remote_only": true, "salary_min": 100000}
    results_count: Mapped[int] = mapped_column(Integer, default=0)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="search_queries")

class ActivityLog(Base):
    __tablename__ = "activity_logs"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    action_type: Mapped[str] = mapped_column(String(50))  # "job_search", "application_created", etc.
    entity_type: Mapped[Optional[str]] = mapped_column(String(50))  # "job", "application"
    entity_id: Mapped[Optional[int]] = mapped_column(Integer)
    details: Mapped[Optional[dict]] = mapped_column(JSON)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Relationships
    user: Mapped["User"] = relationship(back_populates="activity_logs")
```

## API Endpoint Specifications

### REST API Endpoints

```
Authentication (Future Phase)
├─ POST   /api/auth/register
├─ POST   /api/auth/login
└─ POST   /api/auth/logout

Jobs
├─ POST   /api/jobs/search          - Search for jobs
├─ GET    /api/jobs                 - List saved jobs
├─ GET    /api/jobs/{id}            - Get job details
├─ POST   /api/jobs                 - Manually add job
├─ PUT    /api/jobs/{id}            - Update job
├─ DELETE /api/jobs/{id}            - Delete job
└─ POST   /api/jobs/{id}/analyze    - Analyze job requirements (LLM)

Applications
├─ GET    /api/applications         - List all applications (with filters)
├─ GET    /api/applications/{id}    - Get application details
├─ POST   /api/applications         - Create application
├─ PUT    /api/applications/{id}    - Update application
├─ PATCH  /api/applications/{id}/status - Update status only
└─ DELETE /api/applications/{id}    - Delete application

Cover Letters
├─ GET    /api/cover-letters/{id}   - Get cover letter
├─ POST   /api/cover-letters        - Generate cover letter (LLM)
├─ PUT    /api/cover-letters/{id}   - Update cover letter
└─ DELETE /api/cover-letters/{id}   - Delete cover letter

Dashboard
├─ GET    /api/dashboard/stats      - Get dashboard statistics
├─ GET    /api/dashboard/timeline   - Get application timeline
└─ GET    /api/dashboard/activity   - Get recent activity

User Profile
├─ GET    /api/profile              - Get user profile
├─ PUT    /api/profile              - Update profile
└─ POST   /api/profile/resume       - Upload resume

WebSocket
└─ WS     /ws/notifications         - Real-time notifications
```

### API Request/Response Examples

**POST /api/jobs/search**
```json
// Request
{
  "query": "Python Developer",
  "location": "San Francisco, CA",
  "filters": {
    "remote_only": false,
    "employment_type": ["full_time"],
    "salary_min": 100000
  }
}

// Response
{
  "jobs": [
    {
      "id": 123,
      "title": "Senior Python Developer",
      "company": {
        "id": 45,
        "name": "Tech Corp",
        "logo_url": "https://..."
      },
      "location": "San Francisco, CA",
      "remote_policy": "hybrid",
      "salary_min": 120000,
      "salary_max": 180000,
      "employment_type": "full_time",
      "posted_date": "2025-11-20T10:00:00Z",
      "url": "https://...",
      "description": "...",
      "match_score": 85
    }
  ],
  "total": 42,
  "page": 1,
  "per_page": 20
}
```

**POST /api/cover-letters**
```json
// Request
{
  "application_id": 789,
  "style": "professional",  // "professional", "casual", "creative"
  "llm_provider": "claude"  // "claude" or "ollama"
}

// Response
{
  "id": 456,
  "application_id": 789,
  "content": "Dear Hiring Manager,\n\nI am writing to express...",
  "version": 1,
  "llm_provider": "claude",
  "created_at": "2025-11-22T15:30:00Z"
}
```

**GET /api/dashboard/stats**
```json
// Response
{
  "total_applications": 45,
  "by_status": {
    "interested": 12,
    "applied": 20,
    "screening": 5,
    "interview": 6,
    "offer": 1,
    "rejected": 1
  },
  "response_rate": 0.67,
  "avg_response_time_days": 5.2,
  "interviews_this_month": 3,
  "applications_this_week": 8
}
```

## MCP Server Interface Definition

### Tool Definitions

```python
# backend/src/mcp_server/tools.py

from fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("job-manager")

# ============================================================================
# Tool 1: Search Jobs
# ============================================================================

@mcp.tool()
async def search_jobs(
    query: str = Field(description="Job title or keywords (e.g., 'Python Developer')"),
    location: str = Field(description="Geographic location (e.g., 'San Francisco, CA')"),
    remote_only: bool = Field(default=False, description="Filter for remote positions only"),
    max_results: int = Field(default=20, description="Maximum number of results to return")
) -> dict:
    """Search for jobs matching the specified criteria.

    This tool searches across multiple job boards and returns matching positions
    with comprehensive details including salary, requirements, and company info.

    Returns:
        Dictionary containing list of jobs with details, total count, and search metadata.
    """
    # Implementation
    pass

# ============================================================================
# Tool 2: Add Application
# ============================================================================

@mcp.tool()
async def add_application(
    job_id: int = Field(description="ID of the job to apply to"),
    status: str = Field(default="interested", description="Initial status (interested/applied)"),
    notes: str = Field(default="", description="Optional notes about this application")
) -> dict:
    """Track a new job application.

    Creates a new application entry to track your progress with a specific job.
    Can be used for jobs found through search or manually added.

    Returns:
        Created application details including ID and timestamp.
    """
    # Implementation
    pass

# ============================================================================
# Tool 3: Generate Cover Letter
# ============================================================================

@mcp.tool()
async def generate_cover_letter(
    job_description: str = Field(description="Full job description text"),
    user_profile: str = Field(description="User's resume/profile text"),
    style: str = Field(default="professional", description="Writing style: professional/casual/creative")
) -> dict:
    """Generate a tailored cover letter using AI.

    Uses advanced language models to create a customized cover letter that
    highlights relevant experience and addresses specific job requirements.

    Returns:
        Generated cover letter text and metadata.
    """
    # Implementation
    pass

# ============================================================================
# Tool 4: Update Application Status
# ============================================================================

@mcp.tool()
async def update_application_status(
    application_id: int = Field(description="ID of the application to update"),
    new_status: str = Field(description="New status: interested/applied/screening/interview/offer/rejected/accepted/withdrawn"),
    notes: str = Field(default="", description="Optional notes about the status change")
) -> dict:
    """Update the status of a job application.

    Track your progress through the application process by updating the status
    as you move through different stages.

    Returns:
        Updated application details.
    """
    # Implementation
    pass

# ============================================================================
# Tool 5: Get Applications
# ============================================================================

@mcp.tool()
async def get_applications(
    status: str = Field(default="all", description="Filter by status (all/interested/applied/etc.)"),
    company: str = Field(default="", description="Filter by company name"),
    limit: int = Field(default=50, description="Maximum number of applications to return")
) -> dict:
    """Retrieve job applications with optional filters.

    Get a list of your job applications, optionally filtered by status or company.
    Useful for reviewing your application pipeline.

    Returns:
        List of applications matching the filters.
    """
    # Implementation
    pass

# ============================================================================
# Tool 6: Analyze Job Requirements
# ============================================================================

@mcp.tool()
async def analyze_job_requirements(
    job_description: str = Field(description="Full job description text")
) -> dict:
    """Analyze and parse job requirements using AI.

    Extracts structured information from job descriptions including required skills,
    preferred qualifications, experience level, education requirements, and more.

    Returns:
        Structured analysis of job requirements.
    """
    # Implementation
    pass
```

### Resource Definitions

```python
# backend/src/mcp_server/resources.py

@mcp.resource("job://{job_id}")
async def get_job_resource(job_id: int) -> str:
    """Get detailed information about a specific job.

    Returns:
        Formatted job details including description, requirements, company info.
    """
    # Implementation
    pass

@mcp.resource("application://{application_id}")
async def get_application_resource(application_id: int) -> str:
    """Get detailed information about a specific application.

    Returns:
        Formatted application details including status history, notes, cover letters.
    """
    # Implementation
    pass

@mcp.resource("profile://user")
async def get_user_profile() -> str:
    """Get the user's profile and resume.

    Returns:
        Formatted user profile with resume, skills, and preferences.
    """
    # Implementation
    pass

@mcp.resource("stats://dashboard")
async def get_dashboard_stats() -> str:
    """Get dashboard statistics and analytics.

    Returns:
        Formatted statistics about applications, response rates, and trends.
    """
    # Implementation
    pass
```

### Prompt Definitions

```python
# backend/src/mcp_server/prompts.py

@mcp.prompt("job-search-assistant")
async def job_search_assistant_prompt() -> str:
    """Activate the job search assistant.

    Provides context and guidance for searching and tracking jobs.
    """
    return """You are a job search assistant. I can help you:

1. Search for jobs across multiple platforms
2. Track your applications and their status
3. Generate tailored cover letters
4. Analyze job requirements
5. Provide insights on your application pipeline

What would you like to do?"""

@mcp.prompt("cover-letter-writer")
async def cover_letter_writer_prompt() -> str:
    """Activate the cover letter writing assistant.

    Provides context for generating professional cover letters.
    """
    return """I'll help you write a compelling cover letter. Please provide:

1. The job description (or job ID if already saved)
2. Any specific points you want to highlight
3. Preferred tone (professional/casual/creative)

I'll generate a tailored cover letter that emphasizes your relevant experience."""

@mcp.prompt("application-tracker")
async def application_tracker_prompt() -> str:
    """Activate the application tracking assistant.

    Provides overview and management of job applications.
    """
    return """Let me help you track your job applications. I can:

1. Show all your applications and their current status
2. Update application statuses as you progress
3. Provide statistics and insights
4. Set reminders for follow-ups

What would you like to know?"""
```

## Phased Implementation Plan

### Phase 1: Foundation & Setup (Week 1-2)

#### Milestones

**Week 1: Project Structure & Database**
- [ ] Initialize Git repository with conventional commits
- [ ] Set up directory structure
- [ ] Configure backend with FastAPI + uv
- [ ] Configure frontend with React + Vite + TypeScript
- [ ] Set up PostgreSQL with Docker
- [ ] Implement database models (SQLAlchemy)
- [ ] Create Alembic migrations
- [ ] Write initial database tests

**Week 2: Core API & Basic UI**
- [ ] Implement REST API structure
- [ ] Add CORS and middleware configuration
- [ ] Create basic authentication (single-user for MVP)
- [ ] Build React router structure
- [ ] Implement basic layout with TailwindCSS
- [ ] Set up React Query for API calls
- [ ] Add error handling and logging

**Deliverables:**
- Working backend with database
- Basic frontend scaffolding
- Health check endpoints
- Development docker-compose setup

### Phase 2: Job Search & Management (Week 3-4)

#### Milestones

**Week 3: Job Search Engine**
- [ ] Integrate JobSpy API client
- [ ] Implement job search service
- [ ] Add data normalization layer
- [ ] Build deduplication logic
- [ ] Create job search API endpoints
- [ ] Add caching layer (Redis optional)
- [ ] Write job search tests

**Week 4: Job Management UI**
- [ ] Build job search page
- [ ] Implement job cards component
- [ ] Add search filters UI
- [ ] Create job detail modal
- [ ] Implement manual job entry form
- [ ] Add job save/delete functionality
- [ ] Write frontend tests

**Deliverables:**
- Functional job search via API
- Job search and browse UI
- Manual job entry capability

### Phase 3: Application Tracking (Week 5-6)

#### Milestones

**Week 5: Application Backend**
- [ ] Implement application service
- [ ] Create application CRUD endpoints
- [ ] Add status update logic
- [ ] Build activity logging
- [ ] Implement search query history
- [ ] Write application tests

**Week 6: Application UI**
- [ ] Build applications list page
- [ ] Create application detail view
- [ ] Implement status update UI
- [ ] Add timeline/history component
- [ ] Build notes/comments feature
- [ ] Add filters and sorting
- [ ] Write UI tests

**Deliverables:**
- Complete application tracking backend
- Application management UI
- Status tracking with history

### Phase 4: LLM Integration & Cover Letters (Week 7-8)

#### Milestones

**Week 7: LLM Backend**
- [ ] Implement LLM provider abstraction
- [ ] Integrate Claude API
- [ ] Integrate Ollama client
- [ ] Build cover letter generation service
- [ ] Implement job requirement analyzer
- [ ] Add streaming response support
- [ ] Write LLM service tests

**Week 8: Cover Letter UI**
- [ ] Build cover letter generator page
- [ ] Implement markdown editor
- [ ] Add cover letter preview
- [ ] Create version management
- [ ] Build job analysis view
- [ ] Add PDF export (future)
- [ ] Write UI tests

**Deliverables:**
- Dual LLM provider support
- AI cover letter generation
- Job requirement analysis
- Cover letter management UI

### Phase 5: MCP Server Implementation (Week 9)

#### Milestones

**Week 9: MCP Server**
- [ ] Set up FastMCP server
- [ ] Implement all 6 MCP tools
- [ ] Add MCP resources
- [ ] Create MCP prompts
- [ ] Configure transport layer (stdio/HTTP)
- [ ] Write MCP integration tests
- [ ] Create MCP configuration docs
- [ ] Test with Claude Desktop

**Deliverables:**
- Fully functional MCP server
- Integration with Claude Desktop
- MCP configuration documentation

### Phase 6: Dashboard & Analytics (Week 10)

#### Milestones

**Week 10: Dashboard**
- [ ] Build dashboard page
- [ ] Implement statistics API
- [ ] Create charts with Recharts
- [ ] Add application timeline view
- [ ] Build recent activity feed
- [ ] Implement WebSocket notifications
- [ ] Add dark mode toggle
- [ ] Polish UI/UX

**Deliverables:**
- Interactive dashboard with analytics
- Real-time updates via WebSocket
- Dark mode support

### Phase 7: Testing & Polish (Week 11-12)

#### Milestones

**Week 11: Testing**
- [ ] Achieve >80% backend test coverage
- [ ] Complete frontend test suite
- [ ] Run integration tests
- [ ] Perform security audit
- [ ] Load testing (API performance)
- [ ] Fix identified bugs

**Week 12: Polish & Documentation**
- [ ] Code review and refactoring
- [ ] Performance optimization
- [ ] Complete user documentation
- [ ] Write deployment guide
- [ ] Create demo video/screenshots
- [ ] Prepare for release

**Deliverables:**
- Production-ready application
- Complete documentation
- Deployment package

### Phase 8: Deployment (Week 13)

#### Milestones

- [ ] Create production Docker images
- [ ] Write docker-compose for production
- [ ] Set up environment variable management
- [ ] Configure database backups
- [ ] Deploy to production (local/cloud)
- [ ] Monitor and fix deployment issues
- [ ] Create user onboarding guide

**Deliverables:**
- Deployed application
- Deployment documentation
- Monitoring setup

## Testing Strategy

### Backend Testing

```python
# backend/tests/conftest.py - Test fixtures

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

@pytest.fixture
def db_session():
    """Create a test database session."""
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def client(db_session):
    """Create a test client."""
    app.dependency_overrides[get_db] = lambda: db_session
    return TestClient(app)

# backend/tests/test_jobs.py - Example tests

def test_search_jobs(client):
    """Test job search endpoint."""
    response = client.post("/api/jobs/search", json={
        "query": "Python Developer",
        "location": "San Francisco"
    })
    assert response.status_code == 200
    assert "jobs" in response.json()

def test_create_application(client, db_session):
    """Test application creation."""
    # Create job first
    job = Job(title="Test Job", company_id=1, ...)
    db_session.add(job)
    db_session.commit()

    # Create application
    response = client.post("/api/applications", json={
        "job_id": job.id,
        "status": "interested"
    })
    assert response.status_code == 201
```

### Frontend Testing

```typescript
// frontend/src/components/JobCard.test.tsx

import { render, screen } from '@testing-library/react'
import { JobCard } from './JobCard'

describe('JobCard', () => {
  it('renders job information correctly', () => {
    const job = {
      id: 1,
      title: 'Python Developer',
      company: { name: 'Tech Corp' },
      location: 'San Francisco, CA'
    }

    render(<JobCard job={job} />)

    expect(screen.getByText('Python Developer')).toBeInTheDocument()
    expect(screen.getByText('Tech Corp')).toBeInTheDocument()
  })
})
```

### Test Coverage Goals

| Component | Target Coverage |
|-----------|----------------|
| Backend Services | 90%+ |
| API Endpoints | 85%+ |
| Database Models | 80%+ |
| Frontend Components | 75%+ |
| Integration Tests | Core flows |

## Deployment Configuration

### Docker Setup

```dockerfile
# backend/Dockerfile

FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN pip install uv

# Copy dependency files
COPY pyproject.toml .
COPY requirements.txt .

# Install dependencies
RUN uv pip install -r requirements.txt --system

# Copy application
COPY src/ ./src/

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```dockerfile
# frontend/Dockerfile

FROM node:20-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

```yaml
# docker-compose.yml

version: '3.8'

services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: jobmanager
      POSTGRES_USER: jobuser
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U jobuser"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    build: ./backend
    depends_on:
      postgres:
        condition: service_healthy
    environment:
      DATABASE_URL: postgresql://jobuser:${DB_PASSWORD}@postgres:5432/jobmanager
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
      OLLAMA_BASE_URL: ${OLLAMA_BASE_URL:-http://host.docker.internal:11434}
    ports:
      - "8000:8000"
    volumes:
      - ./backend/src:/app/src
      - ./config:/app/config
    command: uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

  frontend:
    build: ./frontend
    depends_on:
      - backend
    ports:
      - "5173:80"
    environment:
      VITE_API_URL: http://localhost:8000

volumes:
  postgres_data:
```

### Environment Variables

```bash
# .env.example

# Database
DB_PASSWORD=your_secure_password_here

# LLM Providers
ANTHROPIC_API_KEY=sk-ant-...
OLLAMA_BASE_URL=http://localhost:11434

# Job Search
JOBSPY_API_KEY=  # If needed

# Application
DEBUG=false
LOG_LEVEL=INFO
CORS_ORIGINS=http://localhost:5173,http://localhost:3000

# Security (future)
SECRET_KEY=your_secret_key_here
JWT_ALGORITHM=HS256
```

## Success Criteria Checklist

Before considering the project complete:

### Functionality
- [ ] Job search retrieves real data from multiple sources
- [ ] Manual job entry works correctly
- [ ] Application tracking works end-to-end
- [ ] Cover letter generation produces high-quality output
- [ ] Both Claude and Ollama LLM providers work
- [ ] MCP server implements all 6 required tools
- [ ] Dashboard displays all metrics and charts
- [ ] Real-time updates via WebSocket function
- [ ] Dark mode toggle works correctly

### Code Quality
- [ ] Backend test coverage >80%
- [ ] Frontend test coverage >75%
- [ ] All linting passes (ruff, ESLint)
- [ ] Type checking passes (mypy, TypeScript)
- [ ] No critical security vulnerabilities
- [ ] Code follows style guides
- [ ] Comprehensive error handling

### Documentation
- [ ] README with clear installation instructions
- [ ] API documentation (auto-generated from OpenAPI)
- [ ] MCP server configuration guide
- [ ] Architecture documentation up-to-date
- [ ] Deployment guide tested and accurate
- [ ] User guide with screenshots
- [ ] Contributing guidelines

### Security
- [ ] No hardcoded credentials
- [ ] Environment variables properly used
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] Rate limiting implemented
- [ ] No sensitive data in repository

### Deployment
- [ ] Docker deployment works
- [ ] Database migrations tested
- [ ] Configuration examples provided
- [ ] Health check endpoints function
- [ ] Logging is informative
- [ ] Error tracking configured

## Risk Management

| Risk | Impact | Probability | Mitigation |
|------|--------|------------|------------|
| JobSpy API unavailability | High | Low | Implement OpenWeb Ninja fallback |
| LLM API rate limits | Medium | Medium | Implement caching, rate limiting |
| Database performance issues | High | Low | Proper indexing, query optimization |
| Browser automation detection | Medium | Medium | Use only selectively, legal disclaimer |
| Scope creep | High | High | Strict phase boundaries, MVP focus |
| Integration complexity | Medium | Medium | Thorough testing, incremental development |

## Next Steps

### Immediate Actions (Post-Approval)

1. **Set up development environment**
   - Install PostgreSQL, Node.js, Python 3.11+
   - Clone repository, create feature branch
   - Initialize backend with uv
   - Initialize frontend with Vite

2. **Create project structure**
   - Implement directory layout
   - Set up Docker containers
   - Configure git hooks (pre-commit)

3. **Begin Phase 1 implementation**
   - Database models
   - API structure
   - Basic frontend

### Decision Points

**Before proceeding, need approval on:**
1. ✅ Hybrid job search strategy (JobSpy + selective scraping + manual)
2. ✅ Technology stack (FastAPI, React, PostgreSQL)
3. ✅ Dual LLM support (Claude + Ollama)
4. ⚠️ Timeline adjustment if needed (8-12 weeks realistic?)
5. ⚠️ Any additional requirements or constraints?

---

## Appendix

### Recommended Development Tools

- **IDE:** VS Code with extensions (Python, TypeScript, Tailwind)
- **API Testing:** Postman or Insomnia
- **Database Client:** DBeaver or pgAdmin
- **Git Client:** Built-in or GitKraken
- **MCP Testing:** MCP Inspector

### Helpful Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [TailwindCSS Documentation](https://tailwindcss.com/)
- [FastMCP Documentation](https://github.com/modelcontextprotocol/python-sdk)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

### Configuration Templates

All configuration templates are available in:
- `config/config.example.yaml` - Application configuration
- `config/mcp-config.example.json` - MCP server configuration
- `.env.example` - Environment variables
- `docker-compose.yml` - Docker orchestration

---

**Document Status:** Complete and ready for review
**Approval Required:** Yes - Phase 1 research deliverable
**Next Action:** Present findings to stakeholder for approval
