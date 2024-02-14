import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, world!"}


@pytest.mark.parametrize(
    "item_id, q, expected_response",
    [
        (1, None, {"item": 1, "q": None}),
        (42, "test", {"item": 42, "q": "test"}),
    ]
)
def test_read_item(item_id, q, expected_response):
    response = client.get(f"/items/{item_id}", params={"q": q})
    assert response.status_code == 200
    assert response.json() == expected_response
