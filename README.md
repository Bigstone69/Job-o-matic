# Job-o-matic

**Enterprise-Grade MCP Job Application Manager**

An AI-powered job application management system with intelligent job search, automated cover letter generation, and comprehensive application tracking. Built with Model Context Protocol (MCP) integration for seamless AI assistance.

## 🎯 Project Status

**Phase 1: Research & Planning** ✅ COMPLETE

All research deliverables have been completed and are ready for review:

1. ✅ [MCP Protocol Documentation Research](docs/mcp-protocol-research.md)
2. ✅ [Job Search Strategy Analysis](docs/job-search-strategy.md)
3. ✅ [Technology Stack Decision](docs/tech-stack-decision.md)
4. ✅ [Implementation Plan](docs/implementation-plan.md)

**Next Step:** Review and approve Phase 1 findings before proceeding to implementation.

## 🚀 Key Features

### Core Capabilities

- **🔍 Intelligent Job Search**
  - Multi-platform job aggregation (LinkedIn, Indeed, Glassdoor, etc.)
  - Hybrid approach: API-first with selective browser automation
  - Manual job entry for network referrals and niche opportunities

- **📊 Application Tracking**
  - Comprehensive status management (Interested → Applied → Interview → Offer)
  - Timeline visualization and progress analytics
  - Activity logging and search history

- **🤖 AI-Powered Cover Letters**
  - Dual LLM support: Claude API OR local Ollama models
  - Context-aware generation using job description + your profile
  - Multiple style options (professional, casual, creative)
  - Version management and iterative refinement

- **🔌 MCP Integration**
  - Full Model Context Protocol server implementation
  - 6 powerful tools for Claude integration
  - Resource exposure for job and application data
  - Slash command prompts for common workflows

- **📈 Interactive Dashboard**
  - Real-time statistics and analytics
  - Application pipeline visualization
  - Response rate tracking
  - Dark mode support

## 🏗️ Proposed Architecture

### Technology Stack

**Backend:**
- FastAPI (high-performance async API)
- PostgreSQL (production-ready database)
- FastMCP (MCP server framework)
- SQLAlchemy ORM
- Dual LLM: Claude API + Ollama

**Frontend:**
- React 18 with TypeScript
- Vite (lightning-fast builds)
- TailwindCSS (modern styling)
- React Query (server state management)
- Recharts (analytics visualization)

**Infrastructure:**
- Docker + docker-compose
- PostgreSQL 16
- Python 3.11+ with uv
- Node.js 20+

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                  React Dashboard (Port 5173)                │
│           Job Search | Applications | Cover Letters         │
└────────────────────────────┬────────────────────────────────┘
                             │ HTTP/WebSocket
                             ▼
┌─────────────────────────────────────────────────────────────┐
│                   FastAPI Backend (Port 8000)               │
│  ┌──────────┐    ┌──────────┐    ┌──────────────┐         │
│  │ REST API │    │ MCP Server│   │   LLM        │         │
│  │ Endpoints│    │ (FastMCP) │   │   Services   │         │
│  └──────────┘    └──────────┘    └──────────────┘         │
└───────┬──────────────────┬─────────────────┬───────────────┘
        │                  │                 │
        ▼                  ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ PostgreSQL   │  │ Claude API   │  │ Job Search   │
│ Database     │  │ + Ollama     │  │ Engine       │
└──────────────┘  └──────────────┘  └──────────────┘
```

## 📚 Documentation

### Phase 1 Research Documents

1. **[MCP Protocol Research](docs/mcp-protocol-research.md)**
   - Latest MCP specification (2025-06-18)
   - Python SDK implementation patterns (v1.14.1)
   - Security best practices and authentication
   - FastMCP framework advantages

2. **[Job Search Strategy](docs/job-search-strategy.md)**
   - API availability analysis (Indeed, LinkedIn, Glassdoor)
   - Ethical web scraping considerations
   - Hybrid approach recommendation
   - Legal and ToS compliance

3. **[Technology Stack Decision](docs/tech-stack-decision.md)**
   - FastAPI vs Flask comparison (FastAPI selected)
   - PostgreSQL vs SQLite analysis (PostgreSQL selected)
   - React vs Vue vs Svelte evaluation (React selected)
   - LLM integration strategy (Claude + Ollama dual support)

4. **[Implementation Plan](docs/implementation-plan.md)**
   - Complete system architecture diagrams
   - Database schema design (ERD + SQLAlchemy models)
   - API endpoint specifications
   - MCP server interface definition
   - 8-week phased implementation timeline
   - Testing strategy and deployment configuration

### Original Requirements

See [claude.md](claude.md) for the complete project specification and requirements.

## 🎯 Success Criteria

This is an **ENTERPRISE-GRADE** application. Every component meets production standards:

- ✅ Clean, maintainable, well-documented code
- ✅ Comprehensive error handling and logging
- ✅ Secure credential management
- ✅ Scalable architecture
- ✅ Full test coverage (>80% backend, >75% frontend)
- ✅ Professional UI/UX with dark mode
- ✅ Complete documentation

## 📋 Research Summary

### MCP Protocol (2025-06-18)

- **Current Version:** Python SDK 1.14.1 (Sept 2025)
- **Framework:** FastMCP 2.0 (production-ready)
- **Transport:** Streamable HTTP (current standard)
- **Security:** OAuth 2.0 required, input validation critical
- **Best Practice:** Type hints + docstrings for auto-tool generation

### Job Search Strategy

**Recommended Approach:** HYBRID

1. **Primary:** JobSpy API (open-source, self-hosted, $5-10/month)
2. **Secondary:** Selective Playwright automation (user opt-in with legal disclaimer)
3. **Fallback:** Manual entry (always available, legally safe)

**Rationale:**
- Legal compliance (API-first approach)
- Comprehensive coverage (multi-platform)
- Cost-effective (<$20/month)
- User flexibility (manual entry option)

### Technology Stack Justification

**FastAPI** (over Flask):
- 5-7x better performance (15,000+ req/s vs 2,000 req/s)
- Native async/await for LLM streaming
- Auto-generated API documentation
- Production-ready from day one

**PostgreSQL** (over SQLite):
- Multi-user concurrency support
- Advanced full-text search (job descriptions)
- JSONB for flexible job metadata
- Production scalability

**React** (over Vue/Svelte):
- Largest ecosystem and dashboard templates
- Enterprise adoption (most companies use React)
- Best TypeScript support
- Future maintainability

**Dual LLM** (Claude + Ollama):
- Claude: Best quality for cover letters
- Ollama: Privacy-first, no API costs, offline capability
- User choice based on needs

## 🗓️ Proposed Implementation Timeline

### Phase 1: Foundation (Week 1-2) ✅ RESEARCH COMPLETE
- Database models and migrations
- API structure and middleware
- Basic React scaffolding
- Docker development environment

### Phase 2: Job Search (Week 3-4)
- JobSpy API integration
- Data normalization and deduplication
- Job search UI with filters
- Manual job entry

### Phase 3: Application Tracking (Week 5-6)
- Application CRUD operations
- Status management and history
- Applications list and detail views
- Notes and timeline

### Phase 4: LLM Integration (Week 7-8)
- Claude API + Ollama integration
- Cover letter generation service
- Job requirement analyzer
- Cover letter management UI

### Phase 5: MCP Server (Week 9)
- FastMCP server implementation
- 6 MCP tools + resources + prompts
- Claude Desktop integration
- MCP testing and documentation

### Phase 6: Dashboard (Week 10)
- Analytics and statistics
- Charts and visualizations
- Real-time WebSocket updates
- Dark mode

### Phase 7: Testing & Polish (Week 11-12)
- Achieve >80% test coverage
- Security audit
- Performance optimization
- Complete documentation

### Phase 8: Deployment (Week 13)
- Production Docker images
- Deployment guide
- User onboarding
- Monitoring setup

**Total Timeline:** 8-13 weeks (depending on scope adjustments)

## 🔐 Security Considerations

- No hardcoded credentials (environment variables only)
- OAuth 2.0 for MCP authentication
- Input validation and sanitization on all endpoints
- SQL injection prevention (parameterized queries)
- Rate limiting for API protection
- Comprehensive audit logging

## 🎨 User Experience Highlights

- **Clean Interface:** Professional TailwindCSS dashboard design
- **Dark Mode:** Built-in support for user preference
- **Real-time Updates:** WebSocket notifications for status changes
- **Responsive Design:** Mobile-friendly interface
- **Fast Performance:** Optimized React + FastAPI stack
- **AI Assistance:** Natural language cover letter generation

## 🚦 Current Status: Awaiting Phase 1 Approval

**Research Complete:** All Phase 1 deliverables finished
**Documents Created:** 4 comprehensive research documents
**Next Step:** Review findings and approve technology decisions

### Key Decisions Requiring Approval

1. ✅ Hybrid job search strategy (JobSpy + selective automation + manual)
2. ✅ Technology stack (FastAPI, React, PostgreSQL)
3. ✅ Dual LLM support (Claude + Ollama)
4. ⚠️ Timeline and resource allocation (8-13 weeks)
5. ⚠️ Additional requirements or scope changes

---

## 📞 Next Actions

### For Stakeholders/Users

1. **Review Research Documents:**
   - Read through the 4 research documents in `docs/`
   - Evaluate technology decisions and rationale
   - Consider timeline and resource requirements

2. **Provide Feedback:**
   - Any concerns about proposed technologies?
   - Timeline adjustments needed?
   - Additional features or requirements?

3. **Approve to Proceed:**
   - If satisfied with research, approve Phase 2 implementation
   - Or request clarifications/changes before proceeding

### For Development Team

Once approved, immediate next steps:

1. Set up development environment
2. Initialize backend with uv + FastAPI
3. Initialize frontend with Vite + React
4. Configure PostgreSQL with Docker
5. Begin Phase 1 implementation (database models)

---

## 📄 License

[To be determined]

## 🤝 Contributing

[Contributing guidelines will be added during implementation]

---

**Project:** Job-o-matic
**Status:** Phase 1 Research Complete
**Version:** 0.1.0 (Pre-implementation)
**Last Updated:** November 22, 2025
