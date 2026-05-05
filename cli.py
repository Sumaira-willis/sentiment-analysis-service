import argparse
import requests

parser = argparse.ArgumentParser(description="CLI for Sentiment Analysis Service")
parser.add_argument("text", type=str, help="Text to analyze")
parser.add_argument("--url", type=str, default="http://localhost:5000/predict")
args = parser.parse_args()

response = requests.post(args.url, json={"text": args.text})
print(response.json())
