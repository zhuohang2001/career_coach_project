
from flask import Flask, jsonify
from scripts.extract_restaurants import save_restaurant_details
from scripts.extract_events import extract_events
from scripts.analyse_ratings import analyze_ratings

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Restaurant Data Processing API is running!"})

@app.route("/process-all", methods=["POST"])
def process_all():
    """Triggers all processing steps: extract restaurants, extract events, analyze ratings."""
    save_restaurant_details()
    extract_events()
    analyze_ratings()
    return jsonify({"message": "All restaurant data processing completed successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
