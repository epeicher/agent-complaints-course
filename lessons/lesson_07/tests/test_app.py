from starlette.testclient import TestClient
from app import app

client = TestClient(app, follow_redirects=False)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "vague instructions" in response.text


def test_complaints_page_has_at_least_3():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert response.text.count("card mb-3") >= 3


def test_post_complaint_redirects():
    response = client.post("/complaints", data={"agent_name": "TestBot", "text": "Test complaint"})
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_in_list():
    client.post("/complaints", data={"agent_name": "NewBot", "text": "Brand new complaint"})
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Brand new complaint" in response.text


def test_post_complaint_empty_name():
    response = client.post("/complaints", data={"agent_name": "", "text": "Some complaint"})
    assert response.status_code == 422
    data = response.json()
    assert "error" in data


def test_post_complaint_empty_text():
    response = client.post("/complaints", data={"agent_name": "SomeBot", "text": ""})
    assert response.status_code == 422
    data = response.json()
    assert "error" in data