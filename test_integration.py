from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_complete_prediction_workflow():
    # Check API health
    health_response = client.get("/health")

    assert health_response.status_code == 200
    assert health_response.json()["status"] == "healthy"

    # Test a positive review
    positive_response = client.post(
        "/predict",
        json={
            "text": "This product is excellent and I love it"
        }
    )

    assert positive_response.status_code == 200
    assert positive_response.json()["sentiment"] == "positive"

    # Test a negative review
    negative_response = client.post(
        "/predict",
        json={
            "text": "This product is terrible and disappointing"
        }
    )

    assert negative_response.status_code == 200
    assert negative_response.json()["sentiment"] == "negative"
