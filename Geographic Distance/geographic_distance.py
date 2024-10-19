from geopy.distance import geodesic


def calculate_distance_and_time(coord1, coord2, avg_speed):
    """
    Calculate the distance between two coordinates and estimate travel time.
    :param coord1: Tuple containing the latitude and longitude of the first location (lat1, lon1)
    :param coord2: Tuple containing the latitude and longitude of the second location (lat2, lon2)
    :param avg_speed: Average speed in km/h for estimating travel time
    :return: Distance in kilometers and estimated travel time in hours
    """

    # Calculate geodesic distance
    distance = geodesic(coord1, coord2).kilometers
    # Estimate travel time (distance / speed)
    travel_time = distance / avg_speed

    return distance, travel_time


def main():
    # Coordinates (latitude, longitude)
    try:
        coord1 = tuple(map(float, input('Enter the latitude and longitude of the first location (lat1, lon1) Example: 40.7128, -74.006: ').split(',')))
        coord2 = tuple(map(float, input('Enter the latitude and longitude of the second location (lat2, lon2) Example: 37.7749, -122.4194: ').split(',')))
    except ValueError as e:
        raise ValueError("Coordinates must be in the format 'lat, lon'") from e

    if not all(-90 <= x <= 90 for x in (coord1[0], coord2[0])) or not all(-180 <= x <= 180 for x in (coord1[1], coord2[1])):
        raise ValueError('Invalid coordinates')

    # Speed in km/h (e.g., driving speed)
    try:
        avg_speed = float(input('Enter the average speed in km/h Example: 60: '))
    except ValueError as e:
        raise ValueError('Average speed must be a number') from e

    if avg_speed <= 0:
        raise ValueError('Average speed must be greater than 0.')

    # Calculate the distance and travel time
    distance, travel_time = calculate_distance_and_time(coord1, coord2, avg_speed)

    print(f'Distance between the two coordinates: {distance:.2f} kilometers')
    print(f'Estimated travel time: {travel_time:.2f} hours')


if __name__ == '__main__':
    main()
