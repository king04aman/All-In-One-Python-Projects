import pytest
from geographic_distance import calculate_distance_and_time


def test_calculate_distance_and_time():
    # Test with valid coordinates and speed
    coord1 = (40.7128, -74.006)
    coord2 = (37.7749, -122.4194)
    avg_speed = 60
    distance, travel_time = calculate_distance_and_time(coord1, coord2, avg_speed)
    assert distance > 0
    assert travel_time > 0


def test_calculate_distance_and_time_invalid_speed():
    # Test with invalid speed (zero)
    coord1 = (40.7128, -74.006)
    coord2 = (37.7749, -122.4194)
    avg_speed = 0
    with pytest.raises(ValueError):
        calculate_distance_and_time(coord1, coord2, avg_speed)


def test_calculate_distance_and_time_invalid_coordinates():
    # Test with invalid coordinates (not tuples)
    coord1 = "40.7128, -74.006"
    coord2 = "37.7749, -122.4194"
    avg_speed = 60
    with pytest.raises(ValueError):
        calculate_distance_and_time(coord1, coord2, avg_speed)


def test_calculate_distance_and_time_same_coordinates():
    # Test with same coordinates
    coord1 = (40.7128, -74.006)
    coord2 = (40.7128, -74.006)
    avg_speed = 60
    distance, travel_time = calculate_distance_and_time(coord1, coord2, avg_speed)
    assert distance == 0
    assert travel_time == 0
