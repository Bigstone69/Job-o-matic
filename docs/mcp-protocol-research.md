# MCP Protocol Documentation Research

**Research Date:** November 22, 2025
**Purpose:** Understand the latest MCP specification and implementation patterns for Job-o-matic

## Executive Summary

The Model Context Protocol (MCP) is an open standard created by Anthropic that enables seamless integration between LLM applications and external data sources and tools. The current specification version is **2025-06-18**, with the Python SDK at version **1.14.1** (released September 18, 2025).

## MCP Core Concepts

### What is MCP?

MCP provides a universal, open standard for connecting AI systems with data sources, replacing fragmented integrations with a single protocol. It standardizes how applications provide context to LLMs through a client-server architecture.

### Three Core Primitives

1. **Resources** - Data and content exposure (like GET endpoints)
   - File contents, database records, API responses
   - Accessible via @ mentions in Claude Code
   - Can contain text, JSON, structured data, etc.

2. **Tools** - Executable functions (like POST endpoints)
   - Query databases, perform web searches, send messages
   - Execute code or produce side effects
   - Model can invoke through the server

3. **Prompts** - Reusable interaction templates
   - Become slash commands in Claude Code
   - Format: `/mcp__servername__promptname`
   - Define common interaction patterns

## Python SDK Implementation

### Installation

```bash
pip install mcp
# or
uv pip install mcp
```

**Current Version:** 1.14.1 (September 2025)
**Specification:** 2025-06-18

### Key Features

- Full MCP specification implementation
- Build MCP clients to connect to any MCP server
- Create MCP servers exposing resources, prompts, and tools
- Standard transports: stdio, SSE, and Streamable HTTP

### SDK Capabilities

**Client Creation:**
- Connect to any MCP server
- Use standard transports (stdio, SSE, Streamable HTTP)

**Server Creation:**
- Expose resources, prompts, and tools
- Handle client connections
- Implement custom business logic

## Best Practices for 2025

### 1. Framework Selection

**FastMCP** (Production-Ready)
- Higher-level framework built on MCP Python SDK
- Define tools via decorators with Python type hints
- FastMCP 2.0 features:
  - Enterprise authentication
  - OpenAPI/REST adapters
  - Testing utilities
  - Production-ready

### 2. Project Structure

```python
# Define MCP server instance in one central place
# Import into each file that defines tools
# Ensures clean and consistent codebase
```

### 3. Logging Best Practices

⚠️ **CRITICAL:** For STDIO-based servers:
- **NEVER** write to stdout - this corrupts JSON-RPC messages
- Use logging libraries that write to stderr or files
- stdout is reserved for protocol communication

### 4. Transport Layer Selection

**Streamable HTTP** (Current Standard - 2025-03-26)
- Replaces older SSE transport
- Better scalability
- Standard authentication support
- Cloud-ready deployment
- **Recommended for:** Production deployments

**STDIO Transport**
- Best for local processes
- CLI tools and desktop applications
- **Recommended for:** Development and local-only deployments

### 5. Tool Implementation Pattern

```python
# FastMCP uses Python type hints and docstrings
# to automatically generate tool definitions
from fastmcp import FastMCP

mcp = FastMCP("job-manager")

@mcp.tool()
def search_jobs(query: str, location: str) -> dict:
    """Search for jobs matching criteria.

    Args:
        query: Job title or keywords
        location: Geographic location

    Returns:
        List of matching jobs
    """
    # Implementation
    pass
```

## Security Considerations

### Authentication

**OAuth 2.0 Support:**
- Claude Code supports OAuth 2.0 for secure connections
- Remote MCP servers must use secure OAuth 2.0
- Certificates from recognized authorities required

**API Usage:**
- Pass `authorization_token` parameter in MCP server definition
- API consumers handle OAuth flow externally
- Token refresh responsibility on API consumer

### Security Warnings

⚠️ **Third-Party Servers:**
- Use at your own risk - Anthropic hasn't verified all servers
- Trust is essential before installation
- Prompt injection risk with untrusted content fetching

⚠️ **Authentication Vulnerabilities (July 2025 Research):**
- Knostic scanned ~2,000 MCP servers exposed to internet
- All verified servers lacked authentication
- Risk of internal tool listings exposure
- Potential sensitive data exfiltration

### Recommended Security Practices

1. **Authentication Requirements:**
   - Require token exchange, OAuth flow, or mutual TLS during handshake
   - Validate client identity (client certificate or DID-based signature)
   - Terminate connection if authentication fails/missing

2. **Credential Management:**
   - Use short-lived tokens with frequent rotation
   - Encrypt credentials at rest (secrets manager)
   - Encrypt in transit (TLS)

3. **Access Control:**
   - Each MCP server acts as gatekeeper to its system
   - Enforce authentication, auditing, authorization
   - Review Claude's tool invocation requests carefully

4. **Input Validation:**
   - Always validate and sanitize user inputs
   - URL whitelisting for web-fetching tools
   - Guard against prompt injection attacks

## Development Tools

### Debugging Tools

**MCP Inspector:**
```bash
uv run mcp dev my_echo_server.py
```

**Debug Logging:**
```bash
MCP_DEBUG=true python my_echo_server.py
```

### Package Management

**Recommended:** Use `uv` for Python project management
- Modern Python package manager
- Significantly faster than pip
- Automatic virtual environment handling

## Architecture Patterns

### Server/Client Architecture

```
┌─────────────┐         MCP Protocol        ┌─────────────┐
│             │◄───────────────────────────►│             │
│  MCP Client │    (stdio/HTTP/SSE)         │  MCP Server │
│  (Claude)   │                             │  (Our App)  │
│             │                             │             │
└─────────────┘                             └──────┬──────┘
                                                   │
                                                   │ Access
                                                   ▼
                                            ┌─────────────┐
                                            │  Resources  │
                                            │  - Jobs DB  │
                                            │  - Config   │
                                            │  - Files    │
                                            └─────────────┘
```

### For Job-o-matic Implementation

**MCP Server Tools (Required):**
1. `search_jobs(query, location, filters)` - Find jobs
2. `add_application(job_data, status)` - Track application
3. `generate_cover_letter(job_description, user_profile)` - Create letter
4. `update_application_status(app_id, status)` - Update tracking
5. `get_applications(filters)` - Retrieve applications
6. `analyze_job_requirements(job_description)` - Parse requirements

**MCP Server Resources:**
- Job listings database
- Application history
- User profile/resume
- Cover letter templates
- Configuration settings

## References and Sources

- [MCP Specification 2025-06-18](https://modelcontextprotocol.io/specification/2025-06-18)
- [MCP Python SDK - GitHub](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Package - PyPI](https://pypi.org/project/mcp/)
- [Building MCP Servers - Medium](https://medium.com/data-engineering-with-dremio/building-a-basic-mcp-server-with-python-4c34c41031ed)
- [MCP Best Practices - IBM](https://ibm.github.io/mcp-context-forge/best-practices/developing-your-mcp-server-python/)
- [Python MCP Server Guide - Real Python](https://realpython.com/python-mcp/)
- [MCP Security Considerations - Medium](https://luxananda.medium.com/day-12-the-anthropics-mcp-as-a-data-agent-security-part-7-96adda7efc88)
- [Claude Code MCP Documentation](https://docs.anthropic.com/en/docs/claude-code/mcp)
- [Model Context Protocol Introduction - Anthropic](https://www.anthropic.com/news/model-context-protocol)

## Key Takeaways for Job-o-matic

1. ✅ Use **FastMCP 2.0** for production-ready server implementation
2. ✅ Implement **Streamable HTTP** transport for scalability
3. ✅ Use **OAuth 2.0** for secure authentication
4. ✅ Follow **type hint + docstring** pattern for tool definitions
5. ✅ Never write to stdout in STDIO mode
6. ✅ Implement comprehensive input validation and sanitization
7. ✅ Use **uv** for dependency management
8. ✅ Leverage MCP Inspector for debugging
9. ✅ Design tools around the 6 core operations identified above
10. ✅ Implement proper access control and audit logging
