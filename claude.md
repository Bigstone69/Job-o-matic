Enterprise-Grade MCP Job Application Manager
PROJECT OVERVIEW
Build a production-ready job application management system with the following capabilities:

Job Search & Discovery: Automated job searching with intelligent data collection
Application Tracking: Comprehensive tracking of all job applications with status management
AI-Powered Cover Letters: Generate tailored motivation letters using LLM assistance
Interactive Dashboard: Local web-based dashboard for visualization and management
Dual LLM Support: Option to use Claude via MCP OR local Ollama models
Job Requirement Analysis: Intelligent parsing and understanding of job descriptions

CRITICAL SUCCESS CRITERIA
This is an ENTERPRISE-GRADE application. Every component MUST meet production standards:

Clean, maintainable, well-documented code
Comprehensive error handling and logging
Secure credential management
Scalable architecture
Full test coverage
Professional UI/UX

PHASE 1: RESEARCH & PLANNING (MANDATORY FIRST STEPS)
Before writing ANY code, you MUST complete the following research tasks:
Research Task 1: MCP Protocol Documentation
bash# Search and study the latest MCP (Model Context Protocol) documentation
# Focus on:
# - Latest MCP specification (2025 version)
# - Python SDK implementation patterns
# - Server/client architecture best practices
# - Tool and resource definitions
# - Authentication and security patterns
Research Task 2: Job Search Strategy Analysis
bash# Research and document the optimal approach for job data collection:
# 1. Evaluate available Job Board APIs (LinkedIn, Indeed, Glassdoor, etc.)
#    - API availability, rate limits, costs, data quality
# 2. Compare browser automation approaches (Playwright, Selenium, Puppeteer)
#    - Pros/cons, detection avoidance, maintenance overhead
# 3. Research hybrid approaches (API + selective scraping)
# 4. Document legal and ethical considerations (ToS compliance)
# 5. Identify best practices for 2025
#
# DELIVERABLE: Create `docs/job-search-strategy.md` with findings and recommendations
Research Task 3: Technology Stack Evaluation
bash# Research and document the optimal tech stack:
# Backend:
# - FastAPI vs Flask for API server
# - SQLite vs PostgreSQL for data persistence
# - Python MCP SDK patterns
# 
# Frontend:
# - React vs Vue vs Svelte for dashboard
# - TailwindCSS for styling
# - Chart libraries for analytics
#
# LLM Integration:
# - Ollama local deployment patterns
# - Claude API via MCP best practices
# - Streaming responses and error handling
#
# DELIVERABLE: Create `docs/tech-stack-decision.md` with rationale
Research Task 4: Create Implementation Plan
bash# After completing research, create a detailed implementation plan:
# DELIVERABLE: `docs/implementation-plan.md` containing:
# - Architecture diagram (ASCII art or mermaid)
# - Component breakdown with dependencies
# - Database schema design
# - API endpoint specifications
# - MCP server interface definition
# - Testing strategy
# - Deployment considerations
```

**⚠️ STOP after Phase 1 and present findings for approval before proceeding to implementation.**

---

## **PHASE 2: PROJECT SETUP**

### **Directory Structure**
```
job-application-manager/
├── CLAUDE.md                    # This file - project guidelines
├── README.md                     # User-facing documentation
├── docs/                         # All documentation
│   ├── architecture.md
│   ├── api-reference.md
│   ├── mcp-server-guide.md
│   └── deployment-guide.md
├── backend/                      # Python backend
│   ├── pyproject.toml           # uv/pip dependencies
│   ├── src/
│   │   ├── api/                 # FastAPI application
│   │   ├── mcp_server/          # MCP server implementation
│   │   ├── models/              # Database models
│   │   ├── services/            # Business logic
│   │   ├── scrapers/            # Job search implementations
│   │   └── llm/                 # LLM integration (Claude/Ollama)
│   └── tests/
├── frontend/                     # Web dashboard
│   ├── package.json
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── utils/
│   └── tests/
├── database/                     # Database schemas and migrations
├── config/                       # Configuration files
│   ├── config.example.yaml
│   └── mcp-config.example.json
└── scripts/                      # Utility scripts
Initial Setup Commands
bash# Backend setup
cd backend
uv init  # or python -m venv venv
uv pip install fastapi uvicorn sqlalchemy pydantic mcp playwright ollama anthropic python-dotenv pyyaml

# Frontend setup
cd frontend
npm create vite@latest . -- --template react
npm install axios react-router-dom @tanstack/react-query tailwindcss recharts lucide-react

# Initialize git
git init
git add .
git commit -m "chore: initial project structure"

PHASE 3: CORE IMPLEMENTATION
3.1: Database Layer
python# backend/src/models/database.py
# REQUIREMENTS:
# - SQLAlchemy ORM with proper relationships
# - Models: Job, Application, CoverLetter, SearchQuery, Company
# - Comprehensive field validation
# - Timestamp tracking (created_at, updated_at)
# - Status enums for applications (Applied, Interview, Rejected, etc.)
# - Foreign key constraints and indexes
3.2: MCP Server Implementation
python# backend/src/mcp_server/server.py
# REQUIREMENTS:
# - Follow latest MCP Python SDK patterns
# - Implement tools:
#   - search_jobs(query, location, filters)
#   - add_application(job_data, status)
#   - generate_cover_letter(job_description, user_profile)
#   - update_application_status(app_id, status)
#   - get_applications(filters)
#   - analyze_job_requirements(job_description)
# - Implement resources for accessing stored data
# - Proper error handling and validation
# - Logging for all operations
3.3: Job Search Engine
python# backend/src/scrapers/job_search.py
# REQUIREMENTS:
# - Implement the strategy decided in Phase 1
# - Support multiple sources (APIs + browser automation)
# - Rate limiting and respectful crawling
# - Data normalization across sources
# - Duplicate detection
# - Robust error handling
# - Progress tracking for long-running searches
3.4: LLM Integration
python# backend/src/llm/llm_service.py
# REQUIREMENTS:
# - Abstract interface for LLM providers
# - Claude implementation (via Anthropic API)
# - Ollama implementation (local)
# - Configuration-based provider selection
# - Streaming support for real-time responses
# - Prompt templates for:
#   - Cover letter generation
#   - Job requirement analysis
#   - Application email drafting
# - Token usage tracking
# - Fallback mechanisms
3.5: FastAPI Backend
python# backend/src/api/main.py
# REQUIREMENTS:
# - RESTful API endpoints for all operations
# - CORS configuration for local development
# - Request validation with Pydantic
# - Authentication/authorization (future-proof design)
# - WebSocket support for real-time updates
# - OpenAPI/Swagger documentation
# - Health check endpoints
# - Comprehensive error responses
3.6: React Dashboard
typescript// frontend/src/App.tsx
// REQUIREMENTS:
// - Pages:
//   - Dashboard (overview, statistics, recent applications)
//   - Job Search (search interface, results)
//   - Applications (table view with filtering/sorting)
//   - Application Detail (timeline, documents, notes)
//   - Cover Letter Generator (form + preview)
//   - Settings (LLM provider config, preferences)
// - Components:
//   - JobCard, ApplicationCard, StatusBadge
//   - SearchFilters, DateRangePicker
//   - MarkdownEditor for cover letters
//   - Charts for application analytics
// - State management with React Query
// - Responsive design (mobile-friendly)
// - Dark mode support
// - Toast notifications for actions

PHASE 4: ADVANCED FEATURES
4.1: Job Requirement Parser
python# backend/src/services/job_analyzer.py
# REQUIREMENTS:
# - Extract structured data from job descriptions:
#   - Required skills (must-have)
#   - Preferred skills (nice-to-have)
#   - Experience level
#   - Education requirements
#   - Salary range (if available)
#   - Benefits
#   - Work arrangement (remote/hybrid/office)
# - Use LLM for intelligent extraction
# - Store parsed data in structured format
# - Match against user profile
# - Generate match score
4.2: Cover Letter Generator
python# backend/src/services/cover_letter_generator.py
# REQUIREMENTS:
# - Context-aware generation:
#   - Job description
#   - Company research (if available)
#   - User's experience and skills
#   - Specific requirements to address
# - Multiple style options (formal, casual, creative)
# - Iterative refinement capability
# - Save drafts and versions
# - Export to PDF/DOCX
4.3: Application Dashboard
typescript// frontend/src/pages/Dashboard.tsx
// REQUIREMENTS:
// - Overview cards:
//   - Total applications
//   - Response rate
//   - Interview pipeline
//   - Recent activity
// - Charts:
//   - Applications over time
//   - Status breakdown (pie chart)
//   - Response time analysis
// - Recent applications list
// - Quick actions (add application, search jobs)
// - Filters and date ranges

PHASE 5: TESTING & QUALITY ASSURANCE
5.1: Backend Tests
python# backend/tests/
# REQUIREMENTS:
# - Unit tests for all services
# - Integration tests for API endpoints
# - MCP server tool tests
# - Database model tests
# - Mock external APIs (job boards, LLM)
# - Test coverage > 80%
# Use pytest, pytest-asyncio, pytest-cov
5.2: Frontend Tests
typescript// frontend/tests/
// REQUIREMENTS:
// - Component tests with React Testing Library
// - Integration tests for user flows
// - API mock with MSW
// - E2E tests with Playwright (critical paths)
// Use Vitest, @testing-library/react
5.3: Code Quality
bash# REQUIREMENTS:
# - Backend: ruff for linting, black for formatting, mypy for type checking
# - Frontend: ESLint, Prettier, TypeScript strict mode
# - Pre-commit hooks for automated checks
# - CI/CD pipeline ready (GitHub Actions config)

PHASE 6: DOCUMENTATION & DEPLOYMENT
6.1: User Documentation
markdown# README.md
# REQUIREMENTS:
# - Clear project description
# - Feature list with screenshots
# - Installation instructions (step-by-step)
# - Configuration guide
# - Usage examples
# - Troubleshooting section
# - Contributing guidelines
# - License
6.2: Developer Documentation
markdown# docs/
# REQUIREMENTS:
# - Architecture overview
# - API documentation (generated from OpenAPI)
# - MCP server guide (tools, resources, configuration)
# - Database schema documentation
# - Development setup guide
# - Testing guide
# - Deployment guide (Docker, manual)
6.3: Deployment Package
dockerfile# Docker setup
# REQUIREMENTS:
# - Multi-stage build for optimization
# - Separate containers for backend/frontend
# - docker-compose.yml for easy deployment
# - Volume mounts for data persistence
# - Environment variable configuration
# - Health checks

CODE QUALITY STANDARDS
Python Code (MUST)

Use type hints for all functions
Docstrings for all classes and public methods (Google style)
Maximum function complexity: 10 (use radon to check)
Maximum line length: 100 characters
No bare except: clauses - always specify exceptions
Use async/await for I/O operations
Dependency injection for testability

TypeScript Code (MUST)

Strict TypeScript mode enabled
Proper interfaces/types for all data structures
No any types (use unknown if necessary)
Props validation for all components
Custom hooks for reusable logic
Proper error boundaries

Git Workflow (MUST)

Conventional Commits format: type(scope): description

Types: feat, fix, docs, style, refactor, test, chore


Meaningful commit messages (explain WHY, not just WHAT)
Branch naming: feature/, bugfix/, docs/
Never commit sensitive data (use .env files)

Security (MUST)

Never hardcode credentials
Use environment variables for configuration
Validate and sanitize all user inputs
Use parameterized queries (prevent SQL injection)
Implement rate limiting on API endpoints
HTTPS for production (document in deployment guide)


CONFIGURATION EXAMPLES
Backend Config (config/config.example.yaml)
yamldatabase:
  url: "sqlite:///./job_manager.db"  # or postgresql://...

llm:
  provider: "claude"  # or "ollama"
  claude:
    api_key_env: "ANTHROPIC_API_KEY"
    model: "claude-sonnet-4-20250514"
  ollama:
    base_url: "http://localhost:11434"
    model: "llama3.2"

job_search:
  method: "hybrid"  # api, browser, hybrid
  rate_limit_delay: 2  # seconds between requests
  max_concurrent: 3

server:
  host: "0.0.0.0"
  port: 8000
  cors_origins: ["http://localhost:5173"]
MCP Config (config/mcp-config.example.json)
json{
  "mcpServers": {
    "job-manager": {
      "command": "uv",
      "args": ["run", "python", "-m", "backend.src.mcp_server"],
      "env": {
        "CONFIG_PATH": "./config/config.yaml"
      }
    }
  }
}

WORKFLOW INSTRUCTIONS
When Starting a New Feature

Create a feature branch: git checkout -b feature/feature-name
Think through the design - write pseudocode in comments first
Implement with tests (TDD where appropriate)
Run tests and linting locally
Update documentation if needed
Commit with conventional commit message
Test the feature end-to-end

When Debugging

Check logs first (backend/logs/, browser console)
Use debugger (don't rely on print statements)
Write a failing test that reproduces the bug
Fix the bug
Verify the test passes
Document the fix in comments if non-obvious

When Refactoring

Ensure tests pass before starting
Make incremental changes
Run tests after each change
Don't change functionality and refactor simultaneously
Update documentation to reflect changes


SUCCESS CHECKLIST
Before considering the project complete, verify:

 All research documents are comprehensive and up-to-date
 Architecture is clearly documented with diagrams
 MCP server implements all required tools and resources
 Both Claude and Ollama LLM providers work correctly
 Job search functionality retrieves real data
 Cover letter generation produces high-quality output
 Application tracking works end-to-end
 Dashboard displays all required metrics and charts
 Manual job entry works correctly
 All tests pass with >80% coverage
 Code meets quality standards (linting, type checking)
 Documentation is complete and accurate
 Configuration examples are provided
 Docker deployment works
 README has clear installation and usage instructions
 No sensitive data in repository
 Error handling is comprehensive
 Logging is informative but not excessive


FINAL NOTES
This is a COMPREHENSIVE project. Focus on:

Quality over speed - enterprise-grade means production-ready
Modularity - each component should be independently testable
Documentation - future you (and others) will thank you
User experience - the dashboard should be intuitive and pleasant
Maintainability - code should be easy to understand and extend

When in doubt, ASK FOR CLARIFICATION before implementing.
Start with Phase 1 research - it's the foundation for everything else!
