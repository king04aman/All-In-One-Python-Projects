import requests
import json
import time

API_KEY = '7e3f21edee540e6110af347b55eb1ab2'
UNIT = 'metric'
BASE_URL = 'https://api.openweathermap.org/data/2.5/find'

def fetch_weather(city):
    try:
        url = f"{BASE_URL}?q={city}&appid={API_KEY}&units={UNIT}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def check_alerts(data, temp_threshold, wind_speed_threshold):
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
    city = input("Enter city name: ")
    temp_threshold = float(input("Enter temperature threshold (°C): "))
    wind_speed_threshold = float(input("Enter wind speed threshold (m/s): "))

    while True:
        weather_data = fetch_weather(city)
        check_alerts(weather_data, temp_threshold, wind_speed_threshold)
        print("Waiting for the next check...")
        # check every hour
        time.sleep(3600) 
if __name__ == "__main__":
    main()
