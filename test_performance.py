from fastapi.testclient import TestClient
from app.main import app
import time

client = TestClient(app)


def test_prediction_performance():
    start_time = time.time()

    for _ in range(100):
        response = client.post(
            "/predict",
            json={"text": "This is a great product"}
        )
        assert response.status_code == 200

    end_time = time.time()
    total_time = end_time - start_time

    print(f"100 requests completed in {total_time:.2f} seconds")

    # Performance benchmark
    assert total_time < 10


def test_multiple_input_requests():
    inputs = [
        "I love this product",
        "This is terrible",
        "Excellent service",
        "I am very happy",
        "This product is disappointing"
    ]

    for text in inputs:
        response = client.post(
            "/predict",
            json={"text": text}
        )

        assert response.status_code == 200
        assert "sentiment" in response.json()
