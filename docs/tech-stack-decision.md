# Technology Stack Decision

**Research Date:** November 22, 2025
**Purpose:** Select optimal technologies for Job-o-matic enterprise-grade implementation

## Executive Summary

After comprehensive evaluation, the recommended technology stack for Job-o-matic is:

- **Backend:** FastAPI + PostgreSQL + FastMCP
- **Frontend:** React + TailwindCSS + Vite
- **LLM:** Dual support (Claude API + Ollama)
- **Deployment:** Docker + docker-compose
- **Development Tools:** uv (Python), npm (Node.js)

This stack prioritizes production-readiness, performance, developer experience, and enterprise-grade scalability.

## Backend Technology Decisions

### 1. API Framework: FastAPI ✅ SELECTED

#### Comparison Matrix

| Feature | FastAPI | Flask |
|---------|---------|-------|
| **Performance** | 15,000-20,000 req/s | 2,000-3,000 req/s |
| **Async Support** | Native (ASGI) | Bolt-on (less performant) |
| **Type Hints** | First-class | Optional |
| **Auto Documentation** | Built-in (OpenAPI) | Manual/extensions |
| **Validation** | Pydantic (automatic) | Manual/WTForms |
| **Learning Curve** | Moderate | Easy |
| **GitHub Stars** | 78,000 | 68,000 |
| **Maturity** | Modern (2018+) | Mature (2010+) |

#### FastAPI Advantages

**Performance:**
- 3,000+ requests per second typical
- 5-7x faster than Flask for concurrent requests
- Native async/await support for I/O operations

**Developer Experience:**
- Automatic API documentation (Swagger UI)
- Type hints enable autocomplete and IDE support
- Pydantic validation catches errors early
- Less boilerplate code

**Modern Stack:**
- Built on Starlette (ASGI)
- Native WebSocket support
- Streaming responses for LLM integration
- Production-ready from day one

**Enterprise Adoption (2025):**
- Uber, Microsoft, Hugging Face, Shopify, Airbnb, ByteDance
- Robinhood: millions of requests per second
- Growing momentum for new projects

#### When FastAPI is Best

✅ Building production-grade RESTful APIs
✅ High concurrency requirements (job searches, LLM calls)
✅ Type safety and auto-documentation needed
✅ Modern async/await patterns
✅ WebSocket for real-time dashboard updates

#### Decision Rationale

For Job-o-matic, FastAPI is optimal because:
1. LLM integrations benefit from async (streaming responses)
2. Multiple concurrent job searches require high performance
3. MCP server integration needs modern async patterns
4. Type safety prevents errors in complex business logic
5. Auto-generated API docs help future development
6. Enterprise-grade from the start (per requirements)

**Verdict:** FastAPI for production-ready, high-performance API server

### 2. Database: PostgreSQL ✅ SELECTED

#### Comparison Matrix

| Feature | PostgreSQL | SQLite |
|---------|-----------|--------|
| **Concurrency** | Excellent (multi-user) | Limited (single writer) |
| **Scalability** | Horizontal + Vertical | Vertical only |
| **Data Integrity** | Advanced constraints | Basic constraints |
| **Full-Text Search** | Built-in (tsvector) | Basic FTS5 |
| **JSON Support** | JSONB (indexed) | JSON (no index) |
| **Deployment** | Server required | File-based |
| **Backups** | Advanced (WAL, PITR) | File copy |
| **Setup Complexity** | Moderate | Minimal |

#### SQLite Use Cases (Not Selected)

✅ Embedded applications (mobile, IoT)
✅ Local-only tools (single user)
✅ Prototyping and testing
✅ No-administration requirement

❌ Multi-user web applications
❌ High write concurrency
❌ Production web services

#### PostgreSQL Use Cases (Selected)

✅ Multi-user web applications
✅ Complex queries and analytics
✅ High concurrency (job searches, application updates)
✅ Data integrity requirements
✅ Advanced indexing (full-text search on job descriptions)
✅ JSON/JSONB for flexible job metadata
✅ Production-ready with enterprise features

#### Decision Rationale

Job-o-matic requirements favor PostgreSQL:

1. **Concurrency:** Multiple job searches + application updates simultaneously
2. **Dashboard Analytics:** Complex queries for charts and statistics
3. **Full-Text Search:** Search job descriptions, companies, skills
4. **JSON Data:** Job metadata varies by source (JSONB perfect fit)
5. **Scalability:** May grow beyond single-user to team features
6. **Data Integrity:** Application tracking requires ACID guarantees
7. **Future-Proof:** Easy to scale up as features expand

**Migration Path:** Start with PostgreSQL directly (avoid SQLite → PostgreSQL migration)

**Deployment:** Docker container (easy local dev + production parity)

**Verdict:** PostgreSQL for production-ready, scalable persistence

### 3. MCP Framework: FastMCP ✅ SELECTED

#### Why FastMCP Over Raw Python SDK

**FastMCP 2.0 Features:**
- Production-ready (explicitly stated)
- Enterprise authentication built-in
- OpenAPI/REST adapters
- Testing utilities
- Decorator-based tool definitions
- Automatic type hint → tool schema generation

**Comparison:**

| Aspect | FastMCP | Raw MCP SDK |
|--------|---------|-------------|
| Development Speed | Fast (decorators) | Slower (manual) |
| Type Safety | Automatic | Manual |
| Testing | Built-in utilities | Custom |
| Documentation | Auto-generated | Manual |
| Production Features | Included | Build yourself |

#### Example FastMCP Implementation

```python
from fastmcp import FastMCP

mcp = FastMCP("job-manager")

@mcp.tool()
async def search_jobs(
    query: str,
    location: str,
    remote_only: bool = False
) -> list[dict]:
    """Search for jobs matching criteria.

    Args:
        query: Job title or keywords
        location: Geographic location
        remote_only: Filter for remote positions only

    Returns:
        List of matching jobs with details
    """
    # Type hints automatically create tool schema
    # Docstring becomes tool description
    results = await job_service.search(query, location, remote_only)
    return results
```

**Verdict:** FastMCP for rapid, production-ready MCP server development

### 4. Python Package Manager: uv ✅ SELECTED

**Why uv over pip/poetry:**
- Significantly faster than pip (10-100x for some operations)
- Automatic virtual environment handling
- Compatible with pip requirements
- Modern, actively developed
- Recommended by MCP documentation

**Usage:**
```bash
uv init
uv pip install fastapi uvicorn sqlalchemy
uv run python main.py
```

**Verdict:** uv for modern, fast Python dependency management

## Frontend Technology Decisions

### 1. Framework: React ✅ SELECTED

#### Comparison Matrix

| Feature | React | Vue | Svelte |
|---------|-------|-----|--------|
| **Bundle Size** | ~40kb | ~20kb | ~1.6kb |
| **Performance** | Good | Good | Excellent |
| **Learning Curve** | Moderate | Easy | Easy |
| **Ecosystem** | Largest | Large | Growing |
| **Enterprise Use** | Extensive | Moderate | Emerging |
| **Dashboard Templates** | Abundant | Good | Limited |
| **TypeScript** | Excellent | Good | Good |
| **Job Market** | High demand | Moderate | Low |

#### Framework Analysis

**Svelte (Best Performance):**
- Compile-time optimization
- Minimal bundle size (1.6kb)
- Excellent performance
- But: Smaller ecosystem, fewer dashboard templates
- Best for: Lightweight apps, performance-critical

**Vue (Balanced):**
- Easy learning curve
- Good documentation
- Moderate ecosystem
- Best for: Fast MVP, smaller teams

**React (Enterprise Choice):**
- Largest ecosystem and community
- Most dashboard templates (Flowbite, TailAdmin, etc.)
- Extensive component libraries
- Best tooling and IDE support
- Highest job market demand
- Most enterprise adoption

#### Decision Rationale for React

Job-o-matic requirements favor React:

1. **Enterprise-Grade:** Project requirement explicitly states enterprise standards
2. **Dashboard Templates:** Abundant TailwindCSS dashboard templates
   - Flowbite Admin: 8.8k stars, React version available
   - TailAdmin: 7 dashboard variations, React support
3. **Component Libraries:**
   - Recharts for analytics charts
   - Headless UI for accessible components
   - React Query for server state
4. **Developer Experience:**
   - Excellent TypeScript support
   - Large knowledge base and tutorials
   - Easy to find experienced developers
5. **Future Maintainability:**
   - Long-term support guaranteed
   - Mature tooling and best practices
6. **Integration:**
   - Vite for fast development
   - React Query for API integration
   - TailwindCSS for styling

**Trade-off:** Slightly larger bundle size vs. ecosystem benefits

**Verdict:** React for enterprise-ready, maintainable dashboard with rich ecosystem

### 2. Build Tool: Vite ✅ SELECTED

**Why Vite:**
- Lightning-fast dev server (esbuild)
- Instant HMR (Hot Module Replacement)
- Optimized production builds
- Native ESM support
- Official React template
- Industry standard for new React projects (2025)

**Setup:**
```bash
npm create vite@latest frontend -- --template react-ts
```

**Verdict:** Vite for modern, fast React development

### 3. Styling: TailwindCSS ✅ SELECTED

**Why TailwindCSS:**
- Utility-first approach (fast development)
- Excellent dashboard templates available
- Dark mode built-in (project requirement)
- Responsive design utilities
- Customizable design system
- Industry standard (2025)

**Dashboard Templates Available:**
- Flowbite Admin Dashboard (React)
- TailAdmin (React, 7 variations)
- Notus React
- All free and open-source

**Verdict:** TailwindCSS for rapid, professional dashboard development

### 4. State Management: React Query + Context ✅ SELECTED

**Architecture:**
- React Query for server state (API calls, caching)
- React Context for client state (UI preferences, theme)
- No Redux (overkill for this app size)

**Why React Query:**
- Automatic caching and revalidation
- Loading/error states built-in
- Optimistic updates
- WebSocket integration support
- Perfect for API-heavy apps

**Verdict:** React Query + Context for optimal state management

### 5. Additional Frontend Libraries

**UI Components:**
- Headless UI (accessible, unstyled components)
- Lucide React (icon library, 1000+ icons)

**Charts/Visualization:**
- Recharts (React-native charts, composable)
- Alternative: Chart.js with react-chartjs-2

**Forms:**
- React Hook Form (performant, minimal re-renders)
- Zod for validation (TypeScript-first)

**Routing:**
- React Router v6 (standard)

**Markdown:**
- React Markdown (cover letter preview/editing)

## LLM Integration Decisions

### Dual Provider Strategy ✅ SELECTED

**Support Both:**
1. **Claude API** (via Anthropic)
2. **Ollama** (local models)

#### Claude API Integration

**Why Claude:**
- High-quality output (cover letters, job analysis)
- Long context window (analyze full job descriptions + resume)
- Function calling for structured outputs
- Official Python SDK

**Implementation:**
```python
from anthropic import AsyncAnthropic

class ClaudeProvider:
    def __init__(self, api_key: str):
        self.client = AsyncAnthropic(api_key=api_key)

    async def generate_cover_letter(
        self,
        job_description: str,
        user_profile: str
    ) -> str:
        response = await self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            messages=[{
                "role": "user",
                "content": f"Job: {job_description}\n\nProfile: {user_profile}\n\nGenerate cover letter:"
            }]
        )
        return response.content[0].text
```

**Pros:**
- Best quality for cover letters
- Reliable, hosted service
- No local hardware requirements

**Cons:**
- API costs (pay per token)
- Requires internet connection
- Data sent to external service

#### Ollama Integration

**Why Ollama:**
- Privacy (all data stays local)
- No per-use costs (free after hardware)
- Offline capability
- Good for testing/development

**Recommended Models:**
- **deepseek-coder-v2** for code analysis
- **llama3.2** for general text generation
- **qwen2.5** for balanced performance

**Implementation:**
```python
import ollama

class OllamaProvider:
    def __init__(self, base_url: str = "http://localhost:11434"):
        self.base_url = base_url

    async def generate_cover_letter(
        self,
        job_description: str,
        user_profile: str,
        model: str = "llama3.2"
    ) -> str:
        response = ollama.generate(
            model=model,
            prompt=f"Job: {job_description}\n\nProfile: {user_profile}\n\nGenerate cover letter:",
            stream=True
        )
        # Stream response for real-time feedback
        full_text = ""
        for chunk in response:
            full_text += chunk['response']
        return full_text
```

**Pros:**
- Complete privacy
- No API costs
- Fast (local)
- Offline capable

**Cons:**
- Requires local GPU (or slower CPU)
- Lower quality than Claude for complex tasks
- User setup complexity

#### Multi-Provider Interface

**Abstraction Layer:**
```python
from abc import ABC, abstractmethod

class LLMProvider(ABC):
    @abstractmethod
    async def generate_cover_letter(
        self,
        job_description: str,
        user_profile: str
    ) -> str:
        pass

    @abstractmethod
    async def analyze_job_requirements(
        self,
        job_description: str
    ) -> JobAnalysis:
        pass

class LLMService:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    async def generate_cover_letter(self, job, profile):
        return await self.provider.generate_cover_letter(
            job_description=job.description,
            user_profile=profile.to_text()
        )

# Configuration-based provider selection
def create_llm_provider(config: dict) -> LLMProvider:
    if config['llm']['provider'] == 'claude':
        return ClaudeProvider(
            api_key=os.getenv(config['llm']['claude']['api_key_env'])
        )
    elif config['llm']['provider'] == 'ollama':
        return OllamaProvider(
            base_url=config['llm']['ollama']['base_url']
        )
    else:
        raise ValueError(f"Unknown provider: {config['llm']['provider']}")
```

**Configuration:**
```yaml
llm:
  provider: "claude"  # or "ollama"

  claude:
    api_key_env: "ANTHROPIC_API_KEY"
    model: "claude-sonnet-4-20250514"

  ollama:
    base_url: "http://localhost:11434"
    model: "llama3.2"
```

**Verdict:** Dual provider support with abstract interface for maximum flexibility

### LLM Best Practices (2025)

**LiteLLM Integration** (Optional Enhancement):
- Multi-provider router (Claude, Ollama, OpenAI, etc.)
- Automatic fallback if primary fails
- Load balancing across providers
- Usage tracking and cost management

**Streaming Support:**
- Real-time feedback for cover letter generation
- Better user experience (see progress)
- Ollama 0.8.0+ supports streaming with tool calls

**Prompt Templates:**
- Versioned prompt library
- A/B testing for quality
- User customization options

## Development Tools

### Version Control: Git ✅ SELECTED

**Best Practices:**
- Conventional commits (enforced)
- Pre-commit hooks (linting, type checking)
- Branch protection on main
- PR reviews for production changes

### Code Quality

**Backend (Python):**
- **Ruff:** Fast linting (replaces flake8, pylint)
- **Black:** Code formatting (uncompromising)
- **mypy:** Static type checking
- **pytest:** Testing framework
- **pytest-cov:** Coverage reports (>80% target)

**Frontend (TypeScript):**
- **ESLint:** Linting (strict config)
- **Prettier:** Code formatting
- **TypeScript:** Strict mode enabled
- **Vitest:** Testing (Vite-native)
- **@testing-library/react:** Component testing

### CI/CD

**GitHub Actions:**
```yaml
# .github/workflows/ci.yml
name: CI

on: [push, pull_request]

jobs:
  backend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v1
      - run: uv pip install -r requirements.txt
      - run: ruff check .
      - run: black --check .
      - run: mypy .
      - run: pytest --cov

  frontend:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm run lint
      - run: npm run type-check
      - run: npm run test
```

## Deployment Stack

### Containerization: Docker ✅ SELECTED

**Multi-Container Architecture:**
```yaml
# docker-compose.yml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: jobmanager
      POSTGRES_USER: jobuser
      POSTGRES_PASSWORD: ${DB_PASSWORD}
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgresql://jobuser:${DB_PASSWORD}@postgres:5432/jobmanager
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY}
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    depends_on:
      - backend
    ports:
      - "5173:80"

volumes:
  postgres_data:
```

**Benefits:**
- Development/production parity
- Easy setup (docker-compose up)
- Isolated environments
- Portable across systems

**Verdict:** Docker + docker-compose for containerized deployment

## Complete Technology Stack Summary

### Backend Stack

```
FastAPI (Web Framework)
├── Uvicorn (ASGI Server)
├── SQLAlchemy (ORM)
│   └── PostgreSQL (Database)
├── Pydantic (Validation)
├── FastMCP (MCP Server)
├── Anthropic SDK (Claude)
├── Ollama Client (Local LLM)
├── Playwright (Browser Automation)
└── Python 3.11+
```

**Dependencies:**
```toml
# pyproject.toml
[project]
dependencies = [
    "fastapi>=0.109.0",
    "uvicorn[standard]>=0.27.0",
    "sqlalchemy>=2.0.25",
    "pydantic>=2.5.0",
    "pydantic-settings>=2.1.0",
    "alembic>=1.13.0",  # Migrations
    "asyncpg>=0.29.0",  # PostgreSQL driver
    "fastmcp>=1.0.0",
    "anthropic>=0.18.0",
    "ollama>=0.2.0",
    "playwright>=1.41.0",
    "python-dotenv>=1.0.0",
    "pyyaml>=6.0.1",
    "httpx>=0.26.0",
]

[project.optional-dependencies]
dev = [
    "ruff>=0.1.14",
    "black>=24.0.0",
    "mypy>=1.8.0",
    "pytest>=7.4.0",
    "pytest-asyncio>=0.23.0",
    "pytest-cov>=4.1.0",
]
```

### Frontend Stack

```
React 18 (UI Framework)
├── Vite (Build Tool)
├── TypeScript (Type Safety)
├── TailwindCSS (Styling)
├── React Router v6 (Routing)
├── React Query (Server State)
├── React Hook Form (Forms)
├── Zod (Validation)
├── Recharts (Charts)
├── Headless UI (Components)
├── Lucide React (Icons)
└── React Markdown (Markdown)
```

**Dependencies:**
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "react-router-dom": "^6.21.0",
    "@tanstack/react-query": "^5.17.0",
    "react-hook-form": "^7.49.0",
    "zod": "^3.22.0",
    "axios": "^1.6.5",
    "recharts": "^2.10.0",
    "@headlessui/react": "^1.7.17",
    "lucide-react": "^0.309.0",
    "react-markdown": "^9.0.0"
  },
  "devDependencies": {
    "@vitejs/plugin-react": "^4.2.0",
    "vite": "^5.0.0",
    "typescript": "^5.3.0",
    "tailwindcss": "^3.4.0",
    "eslint": "^8.56.0",
    "prettier": "^3.1.0",
    "vitest": "^1.1.0",
    "@testing-library/react": "^14.1.0"
  }
}
```

### Infrastructure Stack

```
Docker (Containerization)
├── PostgreSQL 16 (Database)
├── Nginx (Reverse Proxy - optional)
└── Docker Compose (Orchestration)
```

## Decision Confidence Levels

| Decision | Confidence | Flexibility |
|----------|-----------|-------------|
| FastAPI | ⭐⭐⭐⭐⭐ | Low (best choice) |
| PostgreSQL | ⭐⭐⭐⭐⭐ | Low (requirements demand it) |
| React | ⭐⭐⭐⭐ | Medium (Vue viable alternative) |
| TailwindCSS | ⭐⭐⭐⭐⭐ | Low (template ecosystem) |
| FastMCP | ⭐⭐⭐⭐ | Medium (raw SDK alternative) |
| Dual LLM | ⭐⭐⭐⭐⭐ | Low (user flexibility critical) |
| Docker | ⭐⭐⭐⭐⭐ | Low (deployment standard) |

## References and Sources

- [FastAPI vs Flask 2025](https://strapi.io/blog/fastapi-vs-flask-python-framework-comparison)
- [FastAPI Performance Comparison](https://medium.com/@thecodestudio/fastapi-vs-flask-in-2025-what-you-should-actually-be-using-267a5afba9ae)
- [PostgreSQL vs SQLite 2025](https://medium.com/@aayush71727/postgresql-vs-sqlite-in-2025-which-one-belongs-in-production-ddb9815ca5d5)
- [SQLite Use Cases](https://sqlite.org/whentouse.html)
- [React vs Vue vs Svelte 2025](https://medium.com/@ignatovich.dm/react-vs-vue-vs-svelte-choosing-the-right-framework-for-2025-4f4bb9da35b4)
- [Framework Performance 2025](https://medium.com/@jessicajournal/react-vs-vue-vs-svelte-the-ultimate-2025-frontend-performance-comparison-5b5ce68614e2)
- [TailwindCSS Dashboard Templates](https://adminlte.io/blog/tailwind-css-admin-and-dashboard-templates/)
- [Ollama Local LLM Deployment](https://joshuaopolko.com/ollama/)
- [Claude API Integration Guide](https://collabnix.com/claude-api-integration-guide-2025-complete-developer-tutorial-with-code-examples/)
- [Multi-Provider LLM Integration](https://medium.com/@richardhightower/multi-provider-chat-app-litellm-streamlit-ollama-gemini-claude-perplexity-and-modern-llm-afd5218c7eab)

## Final Technology Stack

```
Job-o-matic Technology Stack (2025)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BACKEND
  ├─ Framework: FastAPI 0.109+
  ├─ Database: PostgreSQL 16
  ├─ ORM: SQLAlchemy 2.0
  ├─ MCP: FastMCP 1.0
  ├─ LLM: Claude API + Ollama
  ├─ Automation: Playwright
  └─ Tools: uv, pytest, ruff, mypy

FRONTEND
  ├─ Framework: React 18
  ├─ Build: Vite 5
  ├─ Language: TypeScript 5
  ├─ Styling: TailwindCSS 3
  ├─ State: React Query + Context
  ├─ Charts: Recharts
  └─ Tools: ESLint, Prettier, Vitest

INFRASTRUCTURE
  ├─ Containers: Docker + Compose
  ├─ Database: PostgreSQL 16
  ├─ Proxy: Nginx (optional)
  └─ CI/CD: GitHub Actions

DEVELOPMENT
  ├─ Package Managers: uv, npm
  ├─ Version Control: Git
  ├─ Quality: Ruff, Black, ESLint
  └─ Testing: pytest, Vitest
```

This stack provides the optimal balance of performance, developer experience, production-readiness, and enterprise-grade quality for Job-o-matic.
