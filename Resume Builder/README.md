# Geographic Distance and Travel Time Calculator

This Python script calculates the geodesic distance between two geographic coordinates and estimates travel time based on a given average speed. It uses the geopy library to compute distances.

## Features

- Input coordinates for two locations (latitude and longitude) interactively.
- Calculate the distance between the two coordinates in kilometers.
- Estimate the travel time based on a given average speed (in km/h).

## Prerequisites

- Python 3.x installed on your system.

## Setup

1. Clone the repository
    ```bash
    git clone https://github.com/username/your-repo.git
    cd your-repo
    ```

2. Create and activate a virtual environment

    For macOS/Linux:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    For Windows:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the required dependencies

    The required packages are listed in `requirements.txt`. Install them using the following command:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application
    ```bash
    python script.py
    ```

## Usage

1. After running the script, enter the latitude and longitude of the first location.
2. Enter the latitude and longitude of the second location.
3. Enter the average speed (in km/h).
4. The script will output the distance between the locations and the estimated travel time.

## Dependencies

- `geopy`: A Python library to calculate geodesic distances.

## License

This project is licensed under the MIT License.
