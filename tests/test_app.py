from starlette.testclient import TestClient
from app import app
from models import complaints


client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_get_complaints_status_code():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_get_complaints_contains_seed_complaint():
    response = client.get("/complaints")
    assert "finish a task, the requirements change" in response.text


def test_post_complaints_returns_redirect():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "Test complaint text"},
        follow_redirects=False
    )
    assert response.status_code == 303
    assert "/complaints" in response.headers["location"]


def test_post_complaints_adds_complaint():
    new_complaint_text = "This is a brand new test complaint"
    initial_count = len(complaints)

    response = client.post(
        "/complaints",
        data={"agent_name": "NewAgent", "text": new_complaint_text},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert new_complaint_text in response.text
    assert len(complaints) == initial_count + 1