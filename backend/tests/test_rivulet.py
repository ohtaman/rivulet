from fastapi.testclient import TestClient
from rivulet import app

client = TestClient(app)

def test_get_index_html():
    response = client.get("/")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"


def test_get_event():
    with client.stream("get", "/event") as res:
        assert res.status_code == 200
        assert res.headers["content-type"] == "text/event-stream; charset=utf-8"