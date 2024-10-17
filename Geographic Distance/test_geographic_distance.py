from unittest.mock import patch

import pytest
from geographic_distance import calculate_distance_and_time, main


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


def test_calculate_distance_and_time_same_coordinates():
    # Test with same coordinates
    coord1 = (40.7128, -74.006)
    coord2 = (40.7128, -74.006)
    avg_speed = 60
    distance, travel_time = calculate_distance_and_time(coord1, coord2, avg_speed)
    assert distance == 0
    assert travel_time == 0


@pytest.fixture
def mock_input():
    with patch('builtins.input', side_effect=['40.7128, -74.006', '37.7749, -122.4194', '60']):
        yield


def test_main(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert 'Distance between the two coordinates:' in captured.out
    assert 'Estimated travel time:' in captured.out


def test_main_invalid_coordinates(mock_input, capsys):
    with patch('builtins.input', side_effect=['abc, def', '37.7749, -122.4194', '60']):
        with pytest.raises(ValueError):
            main()


def test_main_invalid_speed(mock_input, capsys):
    with patch('builtins.input', side_effect=['40.7128, -74.006', '37.7749, -122.4194', 'abc']):
        with pytest.raises(ValueError):
            main()


def test_main_zero_speed(mock_input, capsys):
    with patch('builtins.input', side_effect=['40.7128, -74.006', '37.7749, -122.4194', '0']):
        with pytest.raises(ValueError):
            main()


def test_main_same_coordinates(mock_input, capsys):
    with patch('builtins.input', side_effect=['40.7128, -74.006', '40.7128, -74.006', '60']):
        main()
        captured = capsys.readouterr()
        assert 'Distance between the two coordinates: 0.00 kilometers' in captured.out
        assert 'Estimated travel time: 0.00 hours' in captured.out
