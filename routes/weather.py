from flask import Flask, jsonify, request, Blueprint
from utils import open_db, aluno_exists
import requests

app = Flask(__name__)

weather_bp = Blueprint("weather", __name__)

@weather_bp.route('/weather')
def weather():
    aluno_req = request.args.get('aluno')
    if not aluno_req:
        return jsonify(error='Please provide a student name.'), 400

    db = open_db()
    
    aluno = aluno_exists(aluno_req, db)
    if not aluno:
        return jsonify(error='Student not found or name malformed.'), 404

    # Get student's city
    city = aluno.get('city')
    if not city:
        return jsonify(error='Student does not have a registered city.'), 400

    # Find lat and lon by city API
    geocode_url = "https://nominatim.openstreetmap.org/search"
    geocode_params = {
        "q": city,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": "get_weather"}

    geo_resp = requests.get(geocode_url, params=geocode_params, headers=headers)

    if geo_resp.status_code != 200:
        return jsonify(error=f"Geocoding service failed ({geo_resp.status_code})"), 500

    geo_data = geo_resp.json()
    if not geo_data:
        return jsonify(error=f"City '{city}' not found"), 404

    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    # See weather API
    w_url = "https://api.open-meteo.com/v1/forecast"
    w_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": "true"
    }

    wresp = requests.get(w_url, params=w_params)
    if wresp.status_code != 200:
        return jsonify(error=f"Weather service failed ({wresp.status_code})"), 500

    wdata = wresp.json()

    if "current_weather" not in wdata:
        return jsonify({"error": "Weather data not available"}), 500

    current = wdata["current_weather"]

    result = {
        "city": city,
        "temperature_C": current.get("temperature"),
        "windspeed_kmh": current.get("windspeed")
    }

    return jsonify(result)
    