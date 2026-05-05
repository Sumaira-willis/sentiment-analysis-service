from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis")

def predict_sentiment(text: str):
    if not text.strip():
        return {"error": "Empty text"}
    result = sentiment_pipeline(text)[0]
    return {
        "label": result["label"],
        "score": float(result["score"])
    }
