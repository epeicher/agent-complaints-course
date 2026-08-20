from starlette.testclient import TestClient

from app import app

client = TestClient(app)


def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_lists_seed_complaints():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Clippy-9000" in response.text
    assert "The prompt said" in response.text
    assert "make it pop" in response.text


def test_create_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={
            "agent_name": "RedirectCheckerBot",
            "text": "Testing that the redirect actually happens.",
        },
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_new_complaint_appears_after_post():
    client.post(
        "/complaints",
        data={
            "agent_name": "NewlyAddedAgent",
            "text": "This complaint should show up after posting.",
        },
    )
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "NewlyAddedAgent" in response.text
    assert "This complaint should show up after posting." in response.text
