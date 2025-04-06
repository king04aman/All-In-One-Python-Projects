from flask import Flask, render_template, request
import requests
import os
import logging
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable
API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')

if not API_KEY:
    raise ValueError("Missing environment variable 'OPEN_WEATHER_MAP_API_KEY'")

UNIT = 'metric'
BASE_URL = 'https://api.openweathermap.org/data/2.5/find'

# Set up basic logging
logging.basicConfig(level=logging.INFO)

@app.route('/', methods=['GET', 'POST'])
def index():
    alerts = []
    if request.method == 'POST':
        city = request.form.get('city', '').strip()
        if city:
            weather_data = fetch_weather(city)
            alerts = check_alerts(weather_data)
    return render_template('index.html', alerts=alerts)

def fetch_weather(city):
    """Fetches weather data for a given city."""
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNIT}"
    logging.info(f"Fetching weather for {city}: {url}")  # Log the URL being called
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Error fetching data: {response.status_code}, {response.text}")  # Log the error response
        return None

def check_alerts(data):
    """Checks for temperature and wind speed alerts in weather data."""
    if not data or 'list' not in data or not data['list']:
        return ["No data available to check alerts."]

    weather_info = data['list'][0]
    temp = weather_info['main']['temp']
    wind_speed = weather_info['wind']['speed']

    alerts = []
    temp_threshold = float(os.getenv('TEMP_THRESHOLD', 30.0))  # Default to 30°C
    wind_speed_threshold = float(os.getenv('WIND_SPEED_THRESHOLD', 10.0))  # Default to 10 m/s

    if temp > temp_threshold:
        alerts.append(f"Temperature alert! Current temperature: {temp}°C")
    if wind_speed > wind_speed_threshold:
        alerts.append(f"Wind speed alert! Current wind speed: {wind_speed} m/s")

    return alerts if alerts else ["No alerts. Weather conditions are normal."]

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

