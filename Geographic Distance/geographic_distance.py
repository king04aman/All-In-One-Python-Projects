from geopy.distance import geodesic


def calculate_distance_and_time(coord1, coord2, avg_speed):
    """
    Calculate the distance between two coordinates and estimate travel time.
    :param coord1: Tuple containing the latitude and longitude of the first location (lat1, lon1)
    :param coord2: Tuple containing the latitude and longitude of the second location (lat2, lon2)
    :param avg_speed: Average speed in km/h for estimating travel time
    :return: Distance in kilometers and estimated travel time in hours
    """
    if not (isinstance(coord1, tuple) and isinstance(coord2, tuple)):
        raise ValueError("Coordinates must be in the format 'lat, lon'")

    # Calculate geodesic distance
    distance = geodesic(coord1, coord2).kilometers
    # Estimate travel time (distance / speed)
    if avg_speed > 0:
        travel_time = distance / avg_speed
    else:
        raise ValueError("Average speed must be greater than 0.")
    return distance, travel_time


def main():
    # Coordinates (latitude, longitude)
    coord1 = input("Enter the latitude and longitude of the first location (lat1, lon1) Example: 40.7128, -74.006: ")
    coord2 = input("Enter the latitude and longitude of the second location (lat2, lon2) Example: 37.7749, -122.4194: ")

    # Speed in km/h (e.g., driving speed)
    avg_speed = float(input("Enter the average speed in km/h Example: 60: "))

    # Calculate the distance and travel time
    distance, travel_time = calculate_distance_and_time(coord1, coord2, avg_speed)

    print(f"Distance between the two coordinates: {distance:.2f} km")
    print(f"Estimated travel time: {travel_time:.2f} hours")


if __name__ == "__main__":
    main()
