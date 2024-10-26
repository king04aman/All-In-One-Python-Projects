```markdown
# Weather Alert Script 🌦️

A simple Python script that fetches weather data for your city and alerts you if the temperature or wind speed crosses your set thresholds. Perfect for staying on top of weather changes and preparing for unexpected conditions! 🚀

## Features

- **Fetch Weather Data**: Retrieves up-to-date weather information for any city using the OpenWeatherMap API.
- **Custom Alerts**: Set your own temperature and wind speed thresholds. If the weather conditions exceed these, the script will alert you!
- **Hourly Updates**: The script automatically checks the weather every hour, so you’re always in the loop.
- **User Input for City**: Now includes a web form for users to input their desired city, making it easier to get real-time weather alerts for specific locations.
- **Dynamic Web Application**: The application runs on Flask, serving a simple web interface to display alerts.

## Getting Started

### Prerequisites

- Python 3.x
- `requests`, `python-dotenv`, and `Flask` libraries

Install the required libraries using:

```bash
pip install requests python-dotenv Flask
```

## Setup

- Clone or download this repository.
- Get an API key from OpenWeatherMap. (It’s free!)
- Create a `.env` file in the root directory and add your API key like shown in `.env.example`
- To run the web application, execute the following command:

```bash
python main.py
```

- Access the application by navigating to `http://localhost:80` in your web browser.

## Docker Setup

To run the application using Docker:

1. Ensure Docker is installed on your machine.
2. Build the Docker image:

```bash
docker build -t weather-app .
```

3. Run the Docker container:

```bash
docker run -it -p 80:80 -e OPEN_WEATHER_MAP_API_KEY=your_api_key -e CITY="Your City" -e TEMP_THRESHOLD=30 -e WIND_SPEED_THRESHOLD=10 weather-app
```

## Troubleshooting

- **Missing API Key Error**: Double-check that your `.env` file contains the correct `OPEN_WEATHER_MAP_API_KEY`. Make sure there are no typos or extra spaces.
- **Error fetching data**: This could happen if the API key is incorrect or if the city name is misspelled. Verify both and try again.
- **Internal Server Error**: Ensure that the `index.html` file is present in the correct directory and that the Flask app is properly set up to render it.

## Future Improvements

- Consider deploying the application to a cloud platform for wider accessibility.
- Implement AJAX to allow for real-time updates without requiring a page refresh.
- Suggestion: Explore developing this application using Django for better structure and scalability. I would be happy to assist in making improvements in that framework.

