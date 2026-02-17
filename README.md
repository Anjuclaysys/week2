Week 2 Onboarding Plan – FastAPI, Poetry, Virtual Environment, Logging, Debugging, and SQLAlchemy

--------------------------------------------------

Objective:
The goal of Week 2 is to ensure the candidate:
- Understands FastAPI fundamentals
- Uses Poetry and virtual environments properly
- Manages dependencies using pyproject.toml
- Builds REST APIs
- Implements structured logging (JSON logs)
- Uses VS Code debugger effectively
- Understands SQLAlchemy basics
- Pushes code daily to Git

--------------------------------------------------

Reference Links:
- FastAPI Docs: https://fastapi.tiangolo.com/learn/
- Poetry Install Guide: https://python-poetry.org/docs/#installing-with-the-official-installer
- pyproject.toml Guide: https://python-poetry.org/docs/pyproject/
- SQLAlchemy: https://www.sqlalchemy.org/
- FastAPI SQL DB: https://fastapi.tiangolo.com/tutorial/sql-databases/

--------------------------------------------------

Development Setup (Mandatory):

1. Setup virtual environment (venv)
2. Install Poetry using official installer
3. Create project using Poetry (creates pyproject.toml)
4. Manage dependencies using pyproject.toml
5. Install packages using Poetry
6. Configure Uvicorn server
7. Setup VS Code debugging
8. Create .vscode/launch.json for FastAPI debugging

Example Commands:
poetry init
poetry add fastapi uvicorn python-json-logger sqlalchemy
poetry install
poetry shell

--------------------------------------------------

Dependency Management Rules:

- All dependencies must be added using Poetry
- Do NOT use pip install directly
- Maintain pyproject.toml and poetry.lock
- Commit both files to Git
- Keep dependencies minimal

--------------------------------------------------

Daily Task Plan:

Day 1 – FastAPI Setup, Validation, and Debugging

Topics:
- Virtual environment setup
- Poetry configuration
- pyproject.toml structure
- Dependency installation
- VS Code debugging setup
- FastAPI introduction
- Routing
- Path & Query parameters
- Request body
- Pydantic models
- Response models

Tasks:
- Create new FastAPI project using Poetry
- Verify pyproject.toml creation
- Add dependencies using Poetry
- Configure VS Code debugger
- Create APIs:
  - GET /
  - GET /health
  - POST /users
  - GET /users/{id}
  - PUT /users/{id}
- Add input validation
- Add proper error handling
- Run and debug server locally

Deliverable:
- Working FastAPI server
- Validation implemented
- Debug configuration working
- Push to Git

--------------------------------------------------

Day 2 – Logging, Middleware, and Authentication Basics

Topics:
- Python logging module
- python-json-logger
- Log levels and formatting
- FastAPI middleware
- Exception handlers
- JWT basics

Tasks:
- Install python-json-logger using Poetry
- Configure JSON logging
- Log incoming requests and errors
- Add logging middleware
- Implement simple login endpoint
- Generate basic JWT token
- Add protected route example
- Debug auth and logging flow

Deliverable:
- JSON logging working
- Middleware integrated
- Basic auth flow implemented
- Push to Git

--------------------------------------------------

Day 3 – SQLAlchemy Integration and Mid-Week Technical Review

Topics:
- SQLAlchemy basics
- Engine and session
- ORM models
- Table creation
- Basic CRUD operations
- Session management

Tasks:
- Add SQLAlchemy using Poetry
- Configure SQLite database
- Create User model
- Implement basic CRUD with DB
- Replace in-memory storage with DB
- Handle DB session properly

Review (30–45 Minutes Code Walkthrough):
- Review DB configuration
- Check session handling
- Validate model design
- Check dependency injection
- Review logging integration
- Provide improvement suggestions

Deliverable:
- Database integrated APIs
- Working CRUD with SQLAlchemy
- Reviewed and improved code
- Push to Git

--------------------------------------------------

Day 4 – Mini Project

Project:
User Management API Service

Features:
- User CRUD APIs (Database-backed)
- JWT Authentication
- Input validation
- JSON logging
- Middleware
- Dependency management using Poetry
- Debugging support

Deliverable:
- Complete working service
- pyproject.toml + poetry.lock
- JSON logs
- API docs (Swagger)
- Git repository link

--------------------------------------------------

Day 5 – Final Review, Refactoring, and Improvements

Tasks:
- Code cleanup and refactoring
- Improve logging structure
- Improve error handling
- Improve project structure
- Optimize SQLAlchemy usage
- Fix review comments
- Improve documentation
- Performance improvements (if required)

Final Review:
- Full walkthrough of project
- Architecture discussion
- Identify strengths and gaps
- Decide Fast Track or Support Track

Deliverable:
- Clean and improved codebase
- Updated documentation
- Final Git push

--------------------------------------------------