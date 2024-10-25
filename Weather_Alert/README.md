# Weather Alert Script 🌦️

A simple Python script that fetches weather data for your city and alerts you if the temperature or wind speed crosses your set thresholds. Perfect for staying on top of weather changes and preparing for unexpected conditions! 🚀

## Features

- **Fetch Weather Data**: Retrieves up-to-date weather information for any city using the OpenWeatherMap API.
- **Custom Alerts**: Set your own temperature and wind speed thresholds. If the weather conditions exceed these, the script will alert you!
- **Hourly Updates**: The script automatically checks the weather every hour, so you’re always in the loop.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` and `python-dotenv` libraries

Install the required libraries using:

```bash
pip install requests python-dotenv
```

## Setup

- Clone or download this repository.
- Get an API key from OpenWeatherMap. (It’s free!)
- Create a .env file in the root directory and add your API key like shown in `.env.example`
- Run the script

```
python weather_alert.py
```

## Troubleshooting

- Missing API Key Error: Double-check that your .env file contains the correct OPEN_WEATHER_MAP_API_KEY. Make sure there are no typos or extra spaces.
- Error fetching data: This could happen if the API key is incorrect or if the city name is misspelled. Verify both and try again.
