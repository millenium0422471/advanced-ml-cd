from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == "ML Sentiment Analysis API is running"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_positive_sentiment():
    response = client.post(
        "/predict",
        json={"text": "I love this product"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "positive"


def test_negative_sentiment():
    response = client.post(
        "/predict",
        json={"text": "This product is terrible"}
    )

    assert response.status_code == 200
    assert response.json()["sentiment"] == "negative"
