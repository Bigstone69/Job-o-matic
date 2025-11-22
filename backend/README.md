# Job-o-matic Backend

Enterprise-grade FastAPI backend for job application management system.

## Setup

### Prerequisites

- Python 3.11+
- PostgreSQL 16+
- Docker & Docker Compose (recommended)
- uv package manager (recommended) or pip

### Installation

1. **Install dependencies:**

```bash
# Using uv (recommended)
pip install uv
uv pip install -r requirements.txt

# Or using pip
pip install -r requirements.txt
```

2. **Set up environment variables:**

```bash
cp ../.env.example ../.env
# Edit .env with your configuration
```

3. **Start PostgreSQL:**

```bash
# Using Docker Compose (from project root)
docker-compose up -d postgres

# Or install PostgreSQL locally
```

4. **Create database migration:**

```bash
# Create initial migration
alembic revision --autogenerate -m "initial schema"

# Apply migrations
alembic upgrade head
```

5. **Run the development server:**

```bash
# Using uvicorn directly
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Or using Python
python -m src.main
```

The API will be available at:
- **API:** http://localhost:8000
- **API Docs (Swagger):** http://localhost:8000/api/docs
- **API Docs (ReDoc):** http://localhost:8000/api/redoc

## Development

### Code Quality

```bash
# Linting
ruff check src/

# Formatting
black src/

# Type checking
mypy src/

# Run all checks
ruff check src/ && black src/ && mypy src/
```

### Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run with verbose output
pytest -v
```

### Database Migrations

```bash
# Create a new migration
alembic revision --autogenerate -m "description of changes"

# Apply migrations
alembic upgrade head

# Rollback one migration
alembic downgrade -1

# View migration history
alembic history

# View current revision
alembic current
```

## Project Structure

```
backend/
├── src/
│   ├── api/              # API routes and endpoints
│   ├── mcp_server/       # MCP server implementation
│   ├── models/           # Database models
│   ├── services/         # Business logic
│   ├── scrapers/         # Job search implementations
│   ├── llm/              # LLM integration
│   ├── utils/            # Utility functions
│   └── main.py           # FastAPI application
├── tests/                # Test files
├── alembic/              # Database migrations
├── pyproject.toml        # Project configuration
└── requirements.txt      # Dependencies
```

## API Endpoints

### Core Endpoints

- `GET /` - API information
- `GET /health` - Health check
- `GET /api/v1/status` - API status

### Jobs (Coming Soon)

- `POST /api/v1/jobs/search` - Search for jobs
- `GET /api/v1/jobs` - List saved jobs
- `GET /api/v1/jobs/{id}` - Get job details
- `POST /api/v1/jobs` - Manually add job

### Applications (Coming Soon)

- `GET /api/v1/applications` - List applications
- `POST /api/v1/applications` - Create application
- `GET /api/v1/applications/{id}` - Get application
- `PATCH /api/v1/applications/{id}/status` - Update status

### Cover Letters (Coming Soon)

- `POST /api/v1/cover-letters` - Generate cover letter
- `GET /api/v1/cover-letters/{id}` - Get cover letter

## Environment Variables

See `.env.example` for all available environment variables.

Key variables:
- `DB_DATABASE_URL` - PostgreSQL connection string
- `ANTHROPIC_API_KEY` - Claude API key
- `OLLAMA_BASE_URL` - Ollama base URL (default: http://localhost:11434)

## Troubleshooting

### Database Connection Issues

```bash
# Check if PostgreSQL is running
docker ps

# Check database logs
docker logs jobomatic-db

# Test connection
psql -h localhost -U jobuser -d jobmanager
```

### Import Errors

Make sure you're in the backend directory when running commands, or set PYTHONPATH:

```bash
export PYTHONPATH=/path/to/Job-o-matic/backend
```

### Migration Issues

```bash
# Reset database (WARNING: destroys all data)
alembic downgrade base
alembic upgrade head

# Or drop and recreate
docker-compose down -v
docker-compose up -d postgres
alembic upgrade head
```

## Contributing

1. Follow PEP 8 style guide
2. Use type hints for all functions
3. Write docstrings (Google style)
4. Add tests for new features
5. Run linting and tests before committing

## License

[To be determined]
