from flask import Flask, jsonify, request
import joblib
import requests
import pandas as pd

app = Flask(__name__)

# Load trained model & scaler
try:
    model = joblib.load("rainfall_model.pkl")
    scaler = joblib.load("scaler.pkl")
except FileNotFoundError as e:
    print(f"❌ Error loading model or scaler: {e}")
    model = None
    scaler = None

# API details for live rainfall data
API_KEY = "0a78d51d997a1b4a0a822973ff99e173"
WEATHER_API_URL = "https://api.weather.com/v1/rainfall"

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Rainfall Prediction API is running!"})

@app.route("/favicon.ico", methods=["GET"])
def favicon():
    return "", 204  # No Content response for favicon requests

@app.route("/rainfall", methods=["GET"])
def get_rainfall_data():
    location = request.args.get("location", "Austin, TX")
    try:
        response = requests.get(f"{WEATHER_API_URL}?location={location}&key={API_KEY}", timeout=5)
        response.raise_for_status()
        return jsonify(response.json())
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch live rainfall data. Please try again later."}), 500

@app.route("/predict", methods=["GET"])
def predict_rainfall():
    if model is None or scaler is None:
        return jsonify({"error": "Model or scaler not loaded."}), 500

    try:
        # Fetch real-time weather data
        location = request.args.get("location", "Austin, TX")
        weather_response = requests.get(f"{WEATHER_API_URL}?location={location}&key={API_KEY}", timeout=5)
        weather_response.raise_for_status()
        weather_data = weather_response.json()

        # Extract required features
        temperature = weather_data.get("temperature", 0)
        humidity = weather_data.get("humidity", 0)
        pressure = weather_data.get("pressure", 0)

        # Prepare input for the model
        input_data = scaler.transform([[temperature, humidity, pressure]])
        prediction = model.predict(input_data)[0]

        return jsonify({"rainfall_prediction": round(prediction, 2)})
    except KeyError:
        return jsonify({"error": "Failed to extract required weather data."}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to fetch real-time weather data."}), 500
    except Exception as e:
        return jsonify({"error": "An error occurred during prediction."}), 500

@app.route("/locations", methods=["GET"])
def get_locations():
    locations = [
        {"label": "Islamabad, Pakistan", "value": "Islamabad"},
        {"label": "London, UK", "value": "London"},
        {"label": "New York, USA", "value": "New York"}
    ]
    return jsonify(locations)

if __name__ == "__main__":
    app.run(debug=True)