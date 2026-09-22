from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="ONNX Sentiment Analysis API",
    description="Sentiment Analysis API for ML Continuous Delivery",
    version="1.0.0"
)


class TextInput(BaseModel):
    text: str


@app.get("/")
def home():
    return {"message": "ML Sentiment Analysis API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: TextInput):
    text = data.text.lower()

    if not text.strip():
        return {"error": "Text cannot be empty"}

    positive_words = [
        "good",
        "great",
        "excellent",
        "love",
        "happy"
    ]

    sentiment = (
        "positive"
        if any(word in text for word in positive_words)
        else "negative"
    )

    return {
        "text": data.text,
        "sentiment": sentiment
    }
