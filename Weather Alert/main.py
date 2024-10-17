import requests
import json
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Load API key from environment variable (security fix)
API_KEY = os.getenv('OPEN_WEATHER_MAP_API_KEY')

if not API_KEY:
    raise ValueError("Missing environment variable 'OPEN_WEATHER_MAP_API_KEY'")

UNIT = 'metric'
BASE_URL = 'https://api.openweathermap.org/data/2.5/find'


def fetch_weather(city):
    """Fetches weather data for a given city.

    Args:
        city (str): Name of the city.

    Returns:
        dict: Weather data if successful, None otherwise.
    """

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNIT}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching data: {response.status_code}")
        return None


def check_alerts(data, temp_threshold, wind_speed_threshold):
    """Checks for temperature and wind speed alerts in weather data.

    Args:
        data (dict): Weather data.
        temp_threshold (float): Temperature threshold in °C.
        wind_speed_threshold (float): Wind speed threshold in m/s.

    Prints alerts if any, otherwise prints a message indicating normal weather conditions.
    """

    if not data or 'list' not in data or not data['list']:
        print("No data available to check alerts.")
        return

    weather_info = data['list'][0]
    temp = weather_info['main']['temp']
    wind_speed = weather_info['wind']['speed']

    alerts = []
    if temp > temp_threshold:
        alerts.append(f"Temperature alert! Current temperature: {temp}°C")
    if wind_speed > wind_speed_threshold:
        alerts.append(f"Wind speed alert! Current wind speed: {wind_speed} m/s")

    if alerts:
        print("\n".join(alerts))
    else:
        print("No alerts. Weather conditions are normal.")


def main():
    """Prompts user for city name, temperature and wind speed thresholds,
    and continuously checks for alerts.
    """

    city = input("Enter city name: ")
    temp_threshold = float(input("Enter temperature threshold (°C): "))
    wind_speed_threshold = float(input("Enter wind speed threshold (m/s): "))

    while True:
        weather_data = fetch_weather(city)
        check_alerts(weather_data, temp_threshold, wind_speed_threshold)
        print("Waiting for the next check...")
        time.sleep(3600)  # check every hour


if __name__ == "__main__":
    main()