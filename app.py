from flask import Flask, request, jsonify
from model import predict_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Sentiment Analysis Service!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field"}), 400
    return jsonify(predict_sentiment(data["text"]))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
