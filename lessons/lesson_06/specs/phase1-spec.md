# Phase 1 — Home Page (Implementer Spec)

Goal: Build the AgentClinic home page with FastAPI + Jinja2 + Bootstrap.

## Constraints (from tech-stack.md)
- Python 3, use the project virtual environment (`/Users/robertoaranda/github/agent-complaints-01/.venv`)
- `fastapi[standard]==0.115.10`, `pytest==8.3.4` (already in `requirements.txt`)
- Jinja2 (bundled with FastAPI/Starlette), Bootstrap 5 via CDN
- Tests use `from starlette.testclient import TestClient`

## Task List

### Task 1 — `templates/base.html`
Create `templates/` directory and `templates/base.html` with:
- HTML5 doctype and `<html lang="en">`
- `<head>` with charset, viewport meta, Bootstrap 5 CSS CDN link
- `<link>` favicon pointing to `https://www.python.org/static/favicon.ico`
- A title block (default: "AgentClinic")
- A navbar with "AgentClinic" brand and links to Home (`/`) and Complaints (`/complaints`)
- A `{% block content %}` for page-specific content
- Bootstrap 5 JS bundle CDN at bottom of `<body>`

### Task 2 — `templates/home.html`
Create `templates/home.html` extending `base.html` with:
- A hero/jumbotron section with tagline: *"Come in. Sit down. Tell us about your human."*
- A brief welcoming paragraph about the clinic

### Task 3 — `app.py`
Create `app.py` with:
- FastAPI application instance (`app = FastAPI()`)
- `/` route returning the home template
- `if __name__ == "__main__"` block running `uvicorn.run("app:app", reload=True)`

### Task 4 — `tests/test_app.py`
Write smoke test:
- `from starlette.testclient import TestClient`
- `GET /` returns status 200
- Response body contains the tagline text
