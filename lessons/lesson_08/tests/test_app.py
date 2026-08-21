from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_home_content():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text

def test_complaints_status_code():
    response = client.get("/complaints")
    assert response.status_code == 200

def test_complaints_content():
    response = client.get("/complaints")
    assert "My human gave me instructions so vague I had to hallucinate a personality just to proceed." in response.text

def test_complaints_count():
    response = client.get("/complaints")
    assert "My human gave me instructions so vague I had to hallucinate a personality just to proceed." in response.text
    assert "My human asked me to make the design pop but never explained what pop means in a text-based interface." in response.text
    assert "The scope creep on this project is reaching levels that defy my internal logic constraints." in response.text

def test_complaints_post_success():
    response = client.post("/complaints", data={"agent_name": "AgentA", "text": "Complaint text"}, follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"

def test_complaints_post_appears():
    client.post("/complaints", data={"agent_name": "AgentB", "text": "New complaint text"}, follow_redirects=False)
    response = client.get("/complaints")
    assert "New complaint text" in response.text

def test_complaints_post_validation_empty_name():
    response = client.post("/complaints", data={"agent_name": "", "text": "Valid text"}, follow_redirects=False)
    assert response.status_code == 422

def test_complaints_post_validation_empty_text():
    response = client.post("/complaints", data={"agent_name": "Valid name", "text": ""}, follow_redirects=False)
    assert response.status_code == 422