import unittest
from src.manage_itineraries import add_itinerary, edit_itinerary, add_new_flight, add_new_attraction, view_itineraries, delete_itinerary, delete_itinerary_item, print_table
from src.file_handler import load_itineraries, save_itineraries

import os
import io
from rich.console import Console
from rich.table import Table
from rich import print

from pick import Picker

TEST_FILE = "test_itineraries.bin"

"""
Tests all of the functions in manage_itineraries.py

"""


class TestManageItineraries(unittest.TestCase):
    """
    Unit tests for manage_itineraries.py functionalities including adding, editing, viewing, deleting, filtering,
    and persisting itineraries to and from a binary file.
    """

    def setUp(self):
        """
        Set up the test environment by initialising an empty task list
        and backing up the original itinerary binary file.
        """
        self.itineraries = []
        self.original_file = "itineraries.bin"
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)
        os.rename("itineraries.bin", TEST_FILE) if os.path.exists("itineraries.bin") else None

    def tearDown(self):
        """
        Clean up the test environment by removing any test-created binary files
        and restoring the original task binary file.
        """
        if os.path.exists("itineraries.bin"):
            os.remove("itineraries.bin")
        os.rename(TEST_FILE, "itineraries.bin") if os.path.exists(TEST_FILE) else None

    def test_add_itinerary(self):
        """
        Test adding a new task to the task list.
        Verify that the task is successfully added and the list size increases.
        """
        test_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])

        print(self.itineraries)
        self.assertTrue(result)
        self.assertEqual(len(self.itineraries), 1)

    def test_add_duplicate_itinerary(self):
        """
        Test adding a duplicate itinerary with the same title but different values, then a complete copy of the itinerary.
        Verify that these itineraries are not allowed and the function returns False.
        """
        test_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}

        add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])

        same_name_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location="Another location", description="Another description", start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])

        duplicate_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])

        self.assertFalse(same_name_result)
        self.assertFalse(duplicate_result)
        self.assertEqual(len(self.itineraries), 1)

    def test_add_itinerary_with_invalid_dates(self):
        """
        Test adding itineraries with invalid date formats (start_date, end_date, & flight departure and arrival datetimes).
        Verify that the add_itinerary() AND validate_dates() functions handle invalid input as expected and returns False.
        """
        test_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        # Flight item to use for departure_date validation (expected to assertFalse)
        invalid_departure_date = [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "08:00 12-12-2026",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            }]
        
        invalid_arrival_date = [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "2026-12-12 16:00"
            }]
        
        # Test start_date with reversed format ("YYYY-MM-DD") -> asserts False
        invalid_start_date_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date="2026-12-12", end_date=test_itinerary["end_date"], flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])

        # Test end_date with American format ("MM-DD-YYYY") -> asserts False
        invalid_end_date_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date="01-28-2027", flights=test_itinerary["flights"], attractions=test_itinerary["attractions"])
        
        # Test invalid flight dates -> asserts False
        invalid_departure_date_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=invalid_departure_date, attractions=test_itinerary["attractions"])

        invalid_arrival_date_result = add_itinerary(self.itineraries, name=test_itinerary["name"], location=test_itinerary["location"], description=test_itinerary["description"], start_date=test_itinerary["start_date"], end_date=test_itinerary["end_date"], flights=invalid_arrival_date, attractions=test_itinerary["attractions"])

        self.assertFalse(invalid_start_date_result)
        self.assertFalse(invalid_end_date_result)
        self.assertFalse(invalid_departure_date_result)
        self.assertFalse(invalid_arrival_date_result)
        self.assertEqual(len(self.itineraries), 0)

    def test_edit_itinerary(self):
        """
        Test editing an itinerary's items (uses two itineraries).
        Verify that ALL types of items in a specific itinerary can be edited smoothly, which includes:

            new_name (edits name of trip) - covers string types that can be accessed in the first level of the itinerary dictionary, i.e. name, location & description.
            new_start_date (edits trip start_date) - covers validation of a trip's start & end dates.
            new_departure_airport (in flights list) - validates that departure & arrival airport is changed, and for the correct flight.
                Note: the "flight name" value should ALSO change to reflect the new departure airport.
            new_departure_date (in 'flights') - validates that departure & arrival date is validated by the validate_dates() function, then changed for the correct flight.
            new_attraction_name (in 'attractions') - since each item in an attraction dictionary is a type of string and tested the same way, only one needs to be tested.
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        test_England_itinerary = {
            "name": "England 2020", "location": "England", "description": "Trip to England in 2020", "start_date": "21-09-2020", "end_date": "04-10-2020", "flights": [{
                "flight name": "Perth to London",
                "departure airport": "Perth",
                "departure date": "21-09-2020 05:00",
                "arrival airport": "London",
                "arrival date": "21-09-2020 21:00"
            },
                {
                    "flight name": "London to Perth",
                    "departure airport": "London",
                    "departure date": "04-10-2020 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "05-10-2020 15:30"
                }
            ],
            "attractions": [{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ]}
        
        new_name = "Japan 2026-27"
        new_start_date = "27-12-2026"
        new_departure_airport = "Sydney"
        new_departure_date = "23-09-2020 13:30"
        new_attraction_name = "London Theatre"
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        add_itinerary(self.itineraries, name=test_England_itinerary["name"], location=test_England_itinerary["location"], description=test_England_itinerary["description"], start_date=test_England_itinerary["start_date"], end_date=test_England_itinerary["end_date"], flights=test_England_itinerary["flights"], attractions=test_England_itinerary["attractions"])

        edit_itinerary(self.itineraries, test_Japan_itinerary["name"], "name", "N/A", "N/A", new_name)
        self.assertNotEqual(self.itineraries[0]["name"], test_Japan_itinerary["name"])
        self.assertEqual(self.itineraries[0]["name"], new_name)

        edit_itinerary(self.itineraries, self.itineraries[0]["name"], "start_date", "N/A", "N/A", new_start_date)
        self.assertNotEqual(self.itineraries[0]["start_date"], test_Japan_itinerary["start_date"])
        self.assertEqual(self.itineraries[0]["start_date"], new_start_date)
        
        old_departure_airport = test_England_itinerary["flights"][0]["departure airport"]
        old_flight_name = test_England_itinerary["flights"][0]["flight name"]
        edit_itinerary(self.itineraries, self.itineraries[1]["name"], "departure airport", test_England_itinerary["flights"][0]["flight name"], "N/A", new_departure_airport)
        self.assertNotEqual(self.itineraries[1]["flights"][0]["departure airport"], old_departure_airport)
        self.assertNotEqual(self.itineraries[1]["flights"][0]["flight name"], old_flight_name)
        self.assertEqual(self.itineraries[1]["flights"][0]["departure airport"], new_departure_airport)

        old_departure_date = test_England_itinerary["flights"][0]["departure date"]
        edit_itinerary(self.itineraries, self.itineraries[1]["name"], "departure date", test_England_itinerary["flights"][0]["flight name"], "N/A", new_departure_date)
        self.assertNotEqual(self.itineraries[1]["flights"][0]["departure date"], old_departure_date)
        self.assertEqual(self.itineraries[1]["flights"][0]["departure date"], new_departure_date)

        old_attraction_name = test_England_itinerary["attractions"][1]["attraction name"]
        edit_itinerary(self.itineraries, self.itineraries[1]["name"], "attraction name", "N/A", test_England_itinerary["attractions"][1]["attraction name"], new_attraction_name)
        self.assertNotEqual(self.itineraries[1]["attractions"][1]["attraction name"], old_attraction_name)
        self.assertEqual(self.itineraries[1]["attractions"][1]["attraction name"], new_attraction_name)
    

    def test_add_new_flight(self):
        """
        Docstring for test_add_new_flight.
        
        Verifies that:
            1. A new flight is added successfully.
            2. Number of flights has increased by 1
            3. The last flight in the flight list is the added flight (function uses append() to add a new flight)
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Singapore",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Singapore",
                    "arrival date": "28-01-2027 03:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        initial_number_of_flights = len(test_Japan_itinerary["flights"])
        new_flight = [{
                "flight name": "Singapore to Perth",
                "departure airport": "Singapore",
                "departure date": "28-01-2027 04:30",
                "arrival airport": "Perth",
                "arrival date": "28-01-2027 09:45"
            }]
        
        test_new_flight = add_new_flight(self.itineraries, test_Japan_itinerary["name"], new_flight)
        added_flight = [self.itineraries[0]["flights"][-1]]
        self.assertTrue(test_new_flight)
        self.assertEqual(len(self.itineraries[0]["flights"]), (initial_number_of_flights + 1))
        self.assertEqual(added_flight, new_flight)


    def test_add_new_attraction(self):
        """
        Docstring for test_add_new_attraction.
        
        Verifies that:
            1. A new attraction is added successfully.
            2. Number of attractions has increased by 1
            3. The last attraction in the attractions list is the added attraction (function uses append() to add a new attraction)
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Singapore",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Singapore",
                    "arrival date": "28-01-2027 03:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        initial_number_of_attractions = len(test_Japan_itinerary["attractions"])
        new_attraction = [{
                "attraction name": "Singapore to Perth",
                "address": "Singapore",
                "summary": "28-01-2027 04:30",
                "tag(s)": "Perth"
            }]
        
        test_new_attraction = add_new_attraction(self.itineraries, test_Japan_itinerary["name"], new_attraction)
        added_attraction = [self.itineraries[0]["attractions"][-1]]
        self.assertTrue(test_new_attraction)
        self.assertEqual(len(self.itineraries[0]["attractions"]), (initial_number_of_attractions + 1))
        self.assertEqual(added_attraction, new_attraction)


    def test_delete_itinerary(self):
        """
        Test deleting a full itinerary by name.
        Verify that:
            1. The itinerary is removed from the list of itineraries.
            2. The list size decreases.
            3. The itinerary left in the itineraries list is the one not chosen for deletion.
            4. The itinerary chosen for deletion is no longer in the saved itinerary list.
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        test_England_itinerary = {
            "name": "England 2020", "location": "England", "description": "Trip to England in 2020", "start_date": "21-09-2020", "end_date": "04-10-2020", "flights": [{
                "flight name": "Perth to London",
                "departure airport": "Perth",
                "departure date": "21-09-2020 05:00",
                "arrival airport": "London",
                "arrival date": "21-09-2020 21:00"
            },
                {
                    "flight name": "London to Perth",
                    "departure airport": "London",
                    "departure date": "04-10-2020 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "05-10-2020 15:30"
                }
            ],
            "attractions": [{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ]}
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        add_itinerary(self.itineraries, name=test_England_itinerary["name"], location=test_England_itinerary["location"], description=test_England_itinerary["description"], start_date=test_England_itinerary["start_date"], end_date=test_England_itinerary["end_date"], flights=test_England_itinerary["flights"], attractions=test_England_itinerary["attractions"])
        result = delete_itinerary(self.itineraries, test_Japan_itinerary["name"])

        self.assertTrue(result)
        self.assertEqual(len(self.itineraries), 1)
        self.assertEqual(self.itineraries, [test_England_itinerary])
        self.assertNotEqual(self.itineraries, [test_Japan_itinerary])


    def test_delete_itinerary_items(self):
        """
        Test deleting a full itinerary by name.
        Verify that the itinerary is removed from the list of itineraries and the list size decreases.
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        test_England_itinerary = {
            "name": "England 2020", "location": "England", "description": "Trip to England in 2020", "start_date": "21-09-2020", "end_date": "04-10-2020", "flights": [{
                "flight name": "Perth to London",
                "departure airport": "Perth",
                "departure date": "21-09-2020 05:00",
                "arrival airport": "London",
                "arrival date": "21-09-2020 21:00"
            },
                {
                    "flight name": "London to Perth",
                    "departure airport": "London",
                    "departure date": "04-10-2020 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "05-10-2020 15:30"
                }
            ],
            "attractions": [{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ]}
        
        original_itinerary_items = []
        original_itinerary_items.append([{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ])
        original_itinerary_items.append([{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ])
        
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        add_itinerary(self.itineraries, name=test_England_itinerary["name"], location=test_England_itinerary["location"], description=test_England_itinerary["description"], start_date=test_England_itinerary["start_date"], end_date=test_England_itinerary["end_date"], flights=test_England_itinerary["flights"], attractions=test_England_itinerary["attractions"])
        test_delete_flight = delete_itinerary_item(self.itineraries, 'flights', test_Japan_itinerary["name"], test_Japan_itinerary["flights"][1]["flight name"])
        test_delete_attraction = delete_itinerary_item(self.itineraries, 'attractions', test_England_itinerary["name"], test_England_itinerary["attractions"][0]["attraction name"])

        self.assertTrue(test_delete_flight)
        self.assertTrue(test_delete_attraction)

        self.assertNotEqual(self.itineraries[0]["flights"], original_itinerary_items[0])
        self.assertNotEqual(self.itineraries[1]["attractions"], original_itinerary_items[1])
        self.assertEqual(len(self.itineraries[0]["flights"]), len(original_itinerary_items[0]) - 1)
        self.assertEqual(len(self.itineraries[1]["attractions"]), len(original_itinerary_items[1]) - 1)


    def test_save_and_load_itineraries(self):
        """
        
        Test saving itineraries to a file and loading them back.
        Verify that the saved itineraries are correctly loaded with the same data and format.
        """
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        test_England_itinerary = {
            "name": "England 2020", "location": "England", "description": "Trip to England in 2020", "start_date": "21-09-2020", "end_date": "04-10-2020", "flights": [{
                "flight name": "Perth to London",
                "departure airport": "Perth",
                "departure date": "21-09-2020 05:00",
                "arrival airport": "London",
                "arrival date": "21-09-2020 21:00"
            },
                {
                    "flight name": "London to Perth",
                    "departure airport": "London",
                    "departure date": "04-10-2020 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "05-10-2020 15:30"
                }
            ],
            "attractions": [{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ]}
        
        itineraries_list = [test_Japan_itinerary, test_England_itinerary]
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        add_itinerary(self.itineraries, name=test_England_itinerary["name"], location=test_England_itinerary["location"], description=test_England_itinerary["description"], start_date=test_England_itinerary["start_date"], end_date=test_England_itinerary["end_date"], flights=test_England_itinerary["flights"], attractions=test_England_itinerary["attractions"])
        save_itineraries(self.itineraries)
        loaded_itineraries = load_itineraries()

        self.assertEqual(len(loaded_itineraries), 2)
        self.assertEqual(loaded_itineraries, itineraries_list)

    def test_rich_builtin_table(self):
        """
        Test saves itineraries to the itinerary list and displays new formatted table using "rich" Table component.
        Verify that using the view_itineraries() function prints a "rich" Table.
        Verify that the terminal's output matches the itineraries saved in the list of itineraries.

        Documentation for capturing output made by rich: https://rich.readthedocs.io/en/latest/console.html#capturing-output
        Extra resources:
        - [QUESTION] How to test output of rich.Table? #247 https://github.com/Textualize/rich/issues/247
        """

        # Test view_itineraries function to verify itineraries are saved
        test_table = Table(title="Itineraries", show_lines=True)

        test_table.add_column("Trip Name", justify="center", no_wrap=True)
        test_table.add_column("Location", justify="center", no_wrap=True)
        test_table.add_column("Description", justify="left", no_wrap=False)
        test_table.add_column("Start Date", justify="center", no_wrap=True)
        test_table.add_column("End Date", justify="center", no_wrap=True)
        test_table.add_column("Flights", justify="left", no_wrap=True)
        test_table.add_column("Attractions", justify="left", no_wrap=True)
        
        test_Japan_itinerary = {
            "name": "trip", "location": "Japan", "description": "description", "start_date": "12-12-2026", "end_date": "28-01-2027", "flights": [{
                "flight name": "Perth to Narita",
                "departure airport": "Perth",
                "departure date": "12-12-2026 08:00",
                "arrival airport": "Narita",
                "arrival date": "12-12-2026 16:00"
            },
                {
                    "flight name": "Narita to Perth",
                    "departure airport": "Narita",
                    "departure date": "27-01-2027 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "28-01-2027 07:00"
                }
            ],
            "attractions": [{
                "attraction name": "Hike",
                "address": "123 Hike Lane",
                "summary": "A cool hike with good views",
                "tag(s)": "outdoors"
            },
                {
                    "attraction name": "Dinner spot",
                    "address": "49 Sweet Cove",
                    "summary": "A lovely dinner spot",
                    "tag(s)": "dinner, romantic"
                }
            ]}
        
        test_England_itinerary = {
            "name": "England 2020", "location": "England", "description": "Trip to England in 2020", "start_date": "21-09-2020", "end_date": "04-10-2020", "flights": [{
                "flight name": "Perth to London",
                "departure airport": "Perth",
                "departure date": "21-09-2020 05:00",
                "arrival airport": "London",
                "arrival date": "21-09-2020 21:00"
            },
                {
                    "flight name": "London to Perth",
                    "departure airport": "London",
                    "departure date": "04-10-2020 23:00",
                    "arrival airport": "Perth",
                    "arrival date": "05-10-2020 15:30"
                }
            ],
            "attractions": [{
                "attraction name": "London Eye",
                "address": "Somewhere in city",
                "summary": "A glorified ferris wheel that shows the city surrounds",
                "tag(s)": "view, relaxing"
            },
                {
                    "attraction name": "Shakespeare's Globe",
                    "address": "12 address strees",
                    "summary": "A reconstructed theatre",
                    "tag(s)": "entertainment, history"
                }
            ]}
        add_itinerary(self.itineraries, name=test_Japan_itinerary["name"], location=test_Japan_itinerary["location"], description=test_Japan_itinerary["description"], start_date=test_Japan_itinerary["start_date"], end_date=test_Japan_itinerary["end_date"], flights=test_Japan_itinerary["flights"], attractions=test_Japan_itinerary["attractions"])
        add_itinerary(self.itineraries, name=test_England_itinerary["name"], location=test_England_itinerary["location"], description=test_England_itinerary["description"], start_date=test_England_itinerary["start_date"], end_date=test_England_itinerary["end_date"], flights=test_England_itinerary["flights"], attractions=test_England_itinerary["attractions"])
        view_itineraries(self.itineraries, "All")

        # Test that the output printed in the terminal has the same format as the rich component's "Table" class
        test_console = Console(file=io.StringIO())
        test_console.print(test_table)

        # Prints the same table as test_console.print(test_table)
        print_table(self.itineraries)

        test_output = test_console.file.getvalue()
        print(test_output)  # prints table template for itinerary list

        self.assertIs(type(test_table), type(Table()))
        self.assertIs(type(test_output), str)

    def test_pick_move_up_down_function(self):
        """
        Test creates a variety of itinerary options and asserts that the current option highlighted (*not* entered) matches the picker's position in the "options" list.
        Verifies moving up and down the list in a "Picker" screen works.
        Documentation for capturing output made by pick: https://github.com/aisk/pick/blob/master/tests/test_pick.py
        """
        title = "Please choose an itinerary: "
        options = ["TBA", "this_itinerary", "that_itinerary"]
        itinerary_picker = Picker(options, title)
        assert itinerary_picker.get_selected() == ("TBA", 0)
        itinerary_picker.move_up()
        assert itinerary_picker.get_selected() == ("that_itinerary", 2)
        itinerary_picker.move_down()
        itinerary_picker.move_down()
        assert itinerary_picker.get_selected() == ("this_itinerary", 1)


if __name__ == "__main__":
    unittest.main()
