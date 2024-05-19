from fastapi.testclient import TestClient
from rivulet import app

client = TestClient(app)

def test_get_virtual_dom():
    response = client.get("/rivulet")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    data = response.json()
    assert data["tag"] == "div"
    assert len(data["children"]) == 2
    assert data["children"][0]["tag"] == "h1"
    assert data["children"][1]["tag"] == "p"

def test_update_virtual_dom_state():
    update_data = {"content": "New content"}
    response = client.post("/rivulet/state", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["tag"] == "div"
    assert len(data["children"]) == 2
    assert data["children"][0]["tag"] == "h1"
    assert data["children"][1]["tag"] == "p"
    assert data["children"][1]["content"] == "Updated content: New content"
