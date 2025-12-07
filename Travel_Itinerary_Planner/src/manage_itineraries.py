from src.file_handler import save_itineraries
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich import print
"""
This file contains all of the functions needed for the Travel Itinerary Planner.
It allows the user to add, edit, view, delete, and export an itinerary while checking for errors in input.
"""


def add_itinerary(itinerary_list, name, location, description, start_date, end_date, flights, attractions):
    """
    Docstring for add_itinerary

    Returns:
        bool: True if Itinerary is added without issue, otherwise False.

    Side Effects:
        - Saves the updated itinerary list to a file using `save_itineraries`.
    """
    # Print TEST: Uncomment to check that all items have been transferred correctly
    # print(name)
    # print(location)
    # print(description)
    # print(start_date)
    # print(end_date)
    # print(flights)
    # print(attractions)
    # print("TEST ENDS HERE")

    if validate_dates(start_date, end_date, flights):
        # Add the new itinerary after validation checks
        new_itinerary = {
            "name": name,
            "location": location,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "flights": flights,
            "attractions": attractions
        }
        # Uncomment to print for itinerary validation:
        # print(new_itinerary)
        if itinerary_list:
            for itinerary in itinerary_list:
                if new_itinerary == itinerary:
                    print("This itinerary already exists!\nReturning to main menu...")
                    return False
                elif new_itinerary["name"] == itinerary["name"]:
                    print(f"'{new_itinerary["name"]}' already exists!\nReturning to main menu...")
                    return False
                else:
                    itinerary_list.append(new_itinerary)
        else:
            itinerary_list.append(new_itinerary)
        # Uncomment to print for itinerary_list validation:
        # print(itinerary_list)

        save_itineraries(itinerary_list)
        return True
    return False


def edit_itinerary(itinerary_list, itinerary_option, edit_option, flight_choice, attraction_choice, new_value):
    # Edit the itinerary list
    for itinerary in itinerary_list:
        if itinerary["name"] == itinerary_option:
            # Edit DateTime-adjacent data
            if edit_option == "start_date":
                if not validate_dates(new_value, itinerary["end_date"], itinerary["flights"]):
                    print("Invalid date. Format required: DD-MM-YYYY (e.g., 12-12-2026)")
                    return False
                else:
                    itinerary["start_date"] = new_value
                    break
            elif edit_option == "end_date":
                if not validate_dates(itinerary["start_date"], new_value, itinerary["flights"]):
                    print("Invalid date. Format required: DD-MM-YYYY (e.g., 12-12-2026)")
                    return False
                else:
                    itinerary["end_date"] = new_value
                    break
            elif edit_option == "departure date":
                for flight_id in itinerary["flights"]:
                    if flight_id["flight name"] == flight_choice:
                        test_updated_flight = [flight_id]
                        test_updated_flight[0]["departure date"] = new_value
                        if not validate_dates(itinerary["start_date"], itinerary["end_date"], test_updated_flight):
                            print("Invalid date. Format required: DD-MM-YYYY HH:MM (e.g., 12-12-2026 08:00)")
                            return False
                        else:
                            flight_id["departure date"] = new_value
                            break
                break
            elif edit_option == "arrival date":
                for flight_id in itinerary["flights"]:
                    if flight_id["flight name"] == flight_choice:
                        test_updated_flight = [flight_id]
                        test_updated_flight[0]["arrival date"] = new_value
                        if not validate_dates(itinerary["start_date"], itinerary["end_date"], test_updated_flight):
                            print("Invalid date & time. Format required: DD-MM-YYYY HH:MM (e.g., 12-12-2026 08:00")
                            return False
                        else:
                            flight_id["arrival date"] = new_value
                            break
                break
            else:
                # Edit trip's string data (outside of flights & attractions)
                if edit_option == 'name' or edit_option == 'location' or edit_option == 'description':
                    itinerary[edit_option] = new_value
                    break

                # Flights: string type options
                elif edit_option == 'departure airport':
                    for flight_id in itinerary["flights"]:
                        if flight_id["flight name"] == flight_choice:
                            flight_id["departure airport"] = new_value
                            flight_id["flight name"] = f"{new_value} to {flight_id["arrival airport"]}"
                            break
                    break

                elif edit_option == 'arrival airport':
                    for flight_id in itinerary["flights"]:
                        if flight_id["flight name"] == flight_choice:
                            flight_id.update({"arrival airport": new_value})
                            flight_id["flight name"] = f"{flight_id["departure airport"]} to {new_value}"
                            break
                    break

                # Attractions: string type options
                elif edit_option == 'attraction name':
                    for attraction in itinerary["attractions"]:
                        if attraction["attraction name"] == attraction_choice:
                            attraction.update({"attraction name": new_value})
                            break
                    break
                elif edit_option == 'address':
                    for attraction in itinerary["attractions"]:
                        if attraction["attraction name"] == attraction_choice:
                            attraction.update({"address": new_value})
                            break
                    break
                elif edit_option == 'summary':
                    for attraction in itinerary["attractions"]:
                        if attraction["attraction name"] == attraction_choice:
                            attraction.update({"summary": new_value})
                            break
                    break
                elif edit_option == 'tag(s)':
                    for attraction in itinerary["attractions"]:
                        if attraction["attraction name"] == attraction_choice:
                            attraction.update({"tag(s)": new_value})
                            break
                    break
    save_itineraries(itinerary_list)
    # Uncomment to print for itinerary_list validation:
    # print(itinerary_list)
    return True


def add_new_flight(itinerary_list, itinerary_name, new_flights):
    for itinerary in itinerary_list:
        if itinerary["name"] == itinerary_name:
            for flight in new_flights:
                if flight not in itinerary["flights"]:
                    itinerary["flights"].append(flight)
                else:
                    print(f"Duplicate flight detected: {flight["flight name"]}!")
                    print("This flight will not be added.")
                    return False
    save_itineraries(itinerary_list)
    # Uncomment to print for itinerary_list validation:
    # print(itinerary_list)
    return True


def add_new_attraction(itinerary_list, itinerary_name, new_attractions):
    for itinerary in itinerary_list:
        if itinerary["name"] == itinerary_name:
            for attraction in new_attractions:
                if attraction not in itinerary["attractions"]:
                    itinerary["attractions"].append(attraction)
                else:
                    print(f"Duplicate attraction detected: {attraction["attraction name"]}!")
                    print("This attraction will not be added.")
                    return False
    save_itineraries(itinerary_list)
    # Uncomment to print for itinerary_list validation:
    # print(itinerary_list)
    return True


def view_itineraries(itinerary_list, filter_option):
    if filter_option != "All":
        # Filter itinerary list
        filtered_itineraries = []
        for itinerary in itinerary_list:
            if filter_option == itinerary["name"]:
                filtered_itineraries.append(itinerary)
        # Use rich to print table
        print_table(filtered_itineraries)
    else:
        # Use rich to print table
        print_table(itinerary_list)
    return True


def delete_itinerary(itinerary_list, itinerary_to_delete):
    for itinerary in itinerary_list:
        if itinerary["name"] == itinerary_to_delete:
            itinerary_list.remove(itinerary)
            save_itineraries(itinerary_list)
            # Uncomment to print for itinerary_list validation:
            # print(itinerary_list)
            return True
    return False


def delete_itinerary_item(itinerary_list, flights_or_attractions_type, itinerary_name, item_to_delete):
    for itinerary in itinerary_list:
        if itinerary["name"] == itinerary_name:
            if flights_or_attractions_type == "flights":
                for item in itinerary["flights"]:
                    if item["flight name"] == item_to_delete:
                        itinerary["flights"].remove(item)
                        save_itineraries(itinerary_list)
                        return True
            elif flights_or_attractions_type == "attractions":
                for item in itinerary["attractions"]:
                    if item["attraction name"] == item_to_delete:
                        itinerary["attractions"].remove(item)
                        save_itineraries(itinerary_list)
                        return True
    return False


# Print rich table function
def print_table(trips):
    trip_console = Console()
    trip_table = Table(title="Itineraries", show_lines=True)

    trip_table.add_column("Trip Name", justify="center", no_wrap=True)
    trip_table.add_column("Location", justify="center", no_wrap=True)
    trip_table.add_column("Description", justify="center", no_wrap=False)
    trip_table.add_column("Start Date", justify="center", no_wrap=True)
    trip_table.add_column("End Date", justify="center", no_wrap=True)
    trip_table.add_column("Flights", justify="left", no_wrap=True)
    trip_table.add_column("Attractions", justify="left", style="bold", no_wrap=False)

    for trip in trips:
        flight_list = ''
        attraction_list = ''
        if len(trip["flights"]) == 1:
            flight_list = f'[bold red]{trip["flights"][0]["flight name"]}[/bold red] \nDepart: {trip["flights"][0]["departure date"]}\nArrive: {trip["flights"][0]["arrival date"]} \n'
        else:
            for flight in trip["flights"]:
                flight_item = f'[bold red]{flight["flight name"]}[/bold red] \nDepart: {flight["departure date"]}\nArrive: {flight["arrival date"]} \n'
                flight_list = flight_list + f'{flight_item}'

        if len(trip["attractions"]) == 1:
            attraction_list = f'[bold red]{trip["attractions"][0]["attraction name"]}[/bold red] \nAddress: {trip["attractions"][0]["address"]} \nSummary: {trip["attractions"][0]["summary"]} \nTag(s): {trip["attractions"][0]["tag(s)"]}\n'
        else:
            for attraction in trip["attractions"]:
                # Printing python text with colour using ANSI codes: https://vascosim.medium.com/how-to-print-colored-text-in-python-52f6244e2e30
                attraction_string = f'[bold red]{attraction["attraction name"]}[/bold red] \nAddress: {attraction["address"]} \nSummary: {attraction["summary"]} \nTag(s): {attraction["tag(s)"]}\n'
                attraction_list = attraction_list + f'{attraction_string}'

        trip_table.add_row(trip["name"], trip["location"], trip["description"], trip["start_date"], trip["end_date"], flight_list, attraction_list)
    trip_console.print(trip_table)
    return


# Validate dates function
def validate_dates(start_date, end_date, flights):
    """
    Validate dates given for start date, end date and flight datetime

    Raises:
        ValueError: If the start or end date is not in the correct format.

    :param start_date: Itinerary start date.
    :param end_date: Itinerary end date.
    :param flights: Nested dictionary containing flight information. This function will be testing the departure_date and arrival_date items.
    """

    try:
        datetime.strptime(start_date, "%d-%m-%Y")
    except ValueError:
        print("Error: Invalid start date. Use 'DD-MM-YYYY' format.")
        return False

    try:
        datetime.strptime(end_date, "%d-%m-%Y")
    except ValueError:
        print("Error: Invalid end date. Use 'DD-MM-YYYY' format.")
        return False

    # Resource used for following code: https://stackoverflow.com/questions/17322208/multiple-try-codes-in-one-block
    for flight_info in flights:
        try:
            datetime.strptime(flight_info["departure date"], "%d-%m-%Y %H:%M")
        except ValueError:
            print("Error: Invalid date/time for flight departure. Use 'DD-MM-YYYY HH:MM' format.")
            return False

        try:
            datetime.strptime(flight_info["arrival date"], "%d-%m-%Y %H:%M")
        except ValueError:
            print("Error: Invalid date/time for flight arrival. Use 'DD-MM-YYYY HH:MM' format.")
            return False
    return True
