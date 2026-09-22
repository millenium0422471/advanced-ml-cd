from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_empty_text():
    response = client.post(
        "/predict",
        json={"text": ""}
    )
    assert response.status_code == 200
    assert "error" in response.json()


def test_missing_text():
    response = client.post(
        "/predict",
        json={}
    )
    assert response.status_code == 422


def test_invalid_data_type():
    response = client.post(
        "/predict",
        json={"text": 12345}
    )
    assert response.status_code == 422


def test_long_input():
    long_text = "good " * 1000

    response = client.post(
        "/predict",
        json={"text": long_text}
    )

    assert response.status_code == 200


def test_special_characters():
    response = client.post(
        "/predict",
        json={"text": "!@#$%^&*()_+{}[]"}
    )

    assert response.status_code == 200


def test_script_input():
    response = client.post(
        "/predict",
        json={"text": "<script>alert('test')</script>"}
    )

    assert response.status_code == 200
