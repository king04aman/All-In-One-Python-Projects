# Geographic Distance and Travel Time Calculator

This Python script calculates the geodesic distance between two geographic coordinates and estimates travel time based on a given average speed. It uses the geopy library to compute distances.

## Features

-   Input coordinates for two locations (latitude and longitude) interactively.
-   Calculate the distance between the two coordinates in kilometers.
-   Estimate the travel time based on a given average speed (in km/h).

## Prerequisites

-   Python 3.x installed on your system.

## Setup

1. Clone the repository

    ```bash
    git clone https://github.com/king04aman/All-In-One-Python-Projects.git
    cd All-In-One-Python-Projects/Geographic Distance
    ```

2. Create and activate a virtual environment

-   For macOS/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

-   For Windows:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies

    The required packages are listed in requirements.txt. Install them using the following command:

    ```bash
    pip install -r requirements.txt
    ```

    Note: The main dependency is geopy for calculating distances based on geodesic coordinates.

## Usage

1. Run the script:

    ```bash
    python geographic_distance.py
    ```

2. Enter the coordinates (latitude and longitude) of the two locations when prompted.
3. Enter the average speed in km/h to calculate the travel time.

    Example input:

    ```
    Enter the latitude and longitude of the first location (lat1, lon1) Example: 40.7128, -74.006: 52.5200, 13.4050
    Enter the latitude and longitude of the second location (lat2, lon2) Example: 37.7749, -122.4194: 48.8566, 2.3522
    Enter the average speed in km/h Example: 60: 80
    ```

    Example output:

    ```
    Distance between the two coordinates: 878.84 kilometers
    Estimated travel time: 10.99 hours
    ```

## Requirements

Here’s a list of Python dependencies in requirements.txt:

```
geopy==2.2.0
pytest==8.3.3
```
