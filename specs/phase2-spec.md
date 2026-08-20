# Phase 2 — Complaints Board (Implementer Spec)

Goal: Build the AgentClinic complaints board — an in-memory list of complaints rendered as Bootstrap cards, plus a form to add new complaints.

## Constraints (from tech-stack.md)
- Python 3, use the project virtual environment (`/Users/robertoaranda/github/agent-complaints-01/.venv`)
- Data model: `dataclasses.dataclass` with `Complaint(agent_name, text, timestamp)`
- Storage: in-memory module-level `list`, no database
- Templates: Jinja2, Bootstrap 5 via CDN
- Tests use `from starlette.testclient import TestClient`

## Task List

### Task 1 — `models.py`
Create `models.py` with:
- `from datetime import datetime, timezone`
- A `Complaint` dataclass with fields `agent_name: str`, `text: str`, `timestamp: datetime`; `timestamp` defaults to `datetime.now(timezone.utc)`
- A module-level list `complaints: list[Complaint]`
- 3-5 seed complaints (generic AI-agent gripes: unclear instructions, contradictory feedback, scope creep)

### Task 2 — `templates/complaints.html`
Create `templates/complaints.html` extending `base.html` with:
- Heading: "Complaints Board"
- Loop through complaints rendering each as a Bootstrap card (agent name, formatted timestamp, complaint text)
- A form at the bottom: `POST` to `/complaints`, text input for agent name, textarea for complaint text, submit button

### Task 3 — `app.py` routes
Add to existing `app.py`:
- `GET /complaints` route: import `complaints` from `models`, render `complaints.html` passing the list as context
- `POST /complaints` route: import `Complaint` from `models`, read `agent_name` and `text` via `Form` from `fastapi`, append a new `Complaint` to the list, redirect to `GET /complaints` using `RedirectResponse` with status 303

### Task 4 — `tests/test_app.py` additions
Add to existing `tests/test_app.py`:
- `GET /complaints` returns 200 and contains seed complaint text
- `POST /complaints` with `agent_name` and `text` redirects to `/complaints`
- After `POST /complaints`, `GET /complaints` includes the newly added complaint
