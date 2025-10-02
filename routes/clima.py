from flask import Flask, jsonify, request, Blueprint
from utils.functions import open_db, get_aluno
from dotenv import load_dotenv
import requests
import os

load_dotenv()

app = Flask(__name__)

clima_bp = Blueprint("clima", __name__)

@clima_bp.route('/clima')
def clima():
    aluno_req = request.args.get('aluno')
    if not aluno_req:
        return jsonify(error='Please provide a student name.'), 400

    db = open_db()
    
    aluno = get_aluno(aluno_req, db)
    if not aluno:
        return jsonify(error='Student not found or name malformed.'), 404

    aluno_city = aluno.get('city')
    if not aluno_city:
        return jsonify(error='Student does not have a registered city.'), 400

    # Weather API
    w_url = "https://api.weatherapi.com/v1/current.json"
    w_params = {
        "key": os.getenv("WEATHER_KEY"),
        "q": aluno_city,
    }

    # Request data
    wresp = requests.get(w_url, params=w_params)
    if wresp.status_code != 200:
        return jsonify(error=f"Weather service failed ({wresp.status_code})"), 500

    wdata = wresp.json()
    if "current" not in wdata:
        return jsonify({"error": "Weather data not available"}), 500

    current = wdata["current"]

    result = {
        "city": aluno_city,
        "temperature_C": current.get("temp_c"),
        "windspeed_kmh": current.get("wind_kph")
    }

    return jsonify(result)
    