"""
Main FastAPI application for Job-o-matic backend.

This module initializes and configures the FastAPI application with all routes,
middleware, and database connections.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging

from src.models.session import init_db, close_db
from src.api.jobs import router as jobs_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for FastAPI application.

    Handles startup and shutdown events.
    """
    # Startup
    logger.info("Starting Job-o-matic backend...")
    # Note: In production, use Alembic migrations instead of init_db
    # await init_db()  # Uncomment for development only
    logger.info("Job-o-matic backend started successfully")

    yield

    # Shutdown
    logger.info("Shutting down Job-o-matic backend...")
    await close_db()
    logger.info("Job-o-matic backend shutdown complete")


# Create FastAPI application
app = FastAPI(
    title="Job-o-matic API",
    description="Enterprise-grade job application management system API",
    version="0.1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
    lifespan=lifespan,
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",  # Vite dev server
        "http://localhost:3000",  # Alternative frontend
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routers
app.include_router(jobs_router, prefix="/api/v1")


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint - API information."""
    return {
        "name": "Job-o-matic API",
        "version": "0.1.0",
        "status": "running",
        "docs": "/api/docs",
    }


# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint for monitoring."""
    return {"status": "healthy", "service": "job-o-matic-backend"}


# API v1 endpoints placeholder
@app.get("/api/v1/status")
async def api_status():
    """API v1 status endpoint."""
    return {
        "api_version": "v1",
        "status": "operational",
        "features": [
            "job_search",
            "application_tracking",
            "cover_letter_generation",
            "mcp_server",
        ],
    }


# Error handlers
@app.exception_handler(404)
async def not_found_handler(request, exc):
    """Handle 404 errors."""
    return JSONResponse(
        status_code=404,
        content={
            "error": "Not Found",
            "message": f"The requested resource was not found: {request.url.path}",
        },
    )


@app.exception_handler(500)
async def internal_error_handler(request, exc):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal Server Error",
            "message": "An unexpected error occurred. Please try again later.",
        },
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "src.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
