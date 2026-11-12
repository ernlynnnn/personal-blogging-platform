from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_crud_cycle():
    # create
    response = client.post("/articles", json={"title": "Test", "content": "Body", "tags": "a,b"})
    assert response.status_code == 201
    article_id = response.json()["id"]

    # read
    response = client.get(f"/articles/{article_id}")
    assert response.json()["title"] == "Test"

    # list with tag filter
    response = client.get("/articles", params={"tag": "a"})
    assert any(a["id"] == article_id for a in response.json())

    # update
    response = client.put(f"/articles/{article_id}", json={"title": "Edited", "content": "Body", "tags": "a,b"})
    assert response.json()["title"] == "Edited"

    # delete
    assert client.delete(f"/articles/{article_id}").status_code == 204

    # gone
    assert client.get(f"/articles/{article_id}").status_code == 404