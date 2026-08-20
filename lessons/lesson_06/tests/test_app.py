from starlette.testclient import TestClient
from app import app

client = TestClient(app)


def test_home_page_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_returns_200():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_complaints_page_contains_seed():
    response = client.get("/complaints")
    assert "yelled at me for not reading their mind" in response.text


def test_post_complaint_redirects():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "Test complaint"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears():
    unique_text = "Test complaint from test_post_complaint_appears"
    client.post("/complaints", data={"agent_name": "TestAgent", "text": unique_text})
    response = client.get("/complaints")
    assert unique_text in response.text