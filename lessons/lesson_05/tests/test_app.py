from starlette.testclient import TestClient
from app import app
from models import complaints

client = TestClient(app)


def test_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_get_complaints_returns_200():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_get_complaints_contains_seed_text():
    response = client.get("/complaints")
    assert "just make it pop" in response.text


def test_post_complaint_redirects():
    initial_count = len(complaints)
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "Test complaint text"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_shows_new_data():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent2", "text": "Another test complaint"},
        follow_redirects=False,
    )
    assert response.status_code == 303

    response = client.get("/complaints")
    assert response.status_code == 200
    assert "TestAgent2" in response.text
    assert "Another test complaint" in response.text