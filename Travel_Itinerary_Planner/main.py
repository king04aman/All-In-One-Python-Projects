from src.file_handler import load_itineraries
from src.manage_itineraries import add_itinerary, edit_itinerary, add_new_flight, add_new_attraction, view_itineraries, delete_itinerary, delete_itinerary_item, print_table
from pick import pick


def run_app():
    """
    Main loop to run the travel planner.
    """
    itineraries = load_itineraries()
    app_running = True

    while app_running:
        print("Welcome to the Travel Itinerary Planner app!\n")
        print("1. Add a new Itinerary")
        print("2. Edit an existing Itinerary item")
        print("3. Add a new flight/attraction to an existing Itinerary")
        print("4. View existing Itineraries")
        print("5. Delete an Itinerary/Itinerary item")
        print("6. Log out\n")

        # Check user_choice was a number
        while True:
            user_choice = input("Please select one of the above options (1-6): ")
            if user_choice.isdigit():
                choice = int(user_choice)
                if 1 <= choice <= 6:
                    break
                else:
                    print("Enter a number between 1-6.")
            else:
                print("Invalid input: Please enter a number between 1-6.")

        # Add a new itinerary
        if user_choice == "1":
            print("How exciting! Please provide us information about the trip: \n")
            name = input("Name of the itinerary (please choose a name you will remember for later): ")
            location = input("Location (NA if not applicable): ")
            description = input("Brief description of trip: ")
            start_date = input("Start date in DD-MM-YYYY: ")
            end_date = input("End date in DD-MM-YYYY: ")
            flights = []
            attractions = []

            print("\nNow it is time to add flights!")
            user_flight_choice = input("If you want to skip this step, type SKIP and press 'Enter'. Otherwise, press 'Enter'. ")
            flights_list_done = False

            if user_flight_choice == "SKIP":
                flights = []
            else:
                while not flights_list_done:

                    departure_airport = input("Name of the airport you will depart from: ")
                    departure_date = input("Date & time of flight departure (Format: DD-MM-YYYY HH:MM): ")
                    arrival_airport = input("Name of the airport you will arrive at: ")
                    arrival_date = input("Date & time of flight arrival (Format: DD-MM-YYYY HH:MM): ")
                    flight_name = f"{departure_airport} to {arrival_airport}"

                    flights.append({
                        "flight name": flight_name,
                        "departure airport": departure_airport,
                        "departure date": departure_date,
                        "arrival airport": arrival_airport,
                        "arrival date": arrival_date
                        })

                    while True:
                        add_another_flight = input("Would you like to add another flight? Type Y (yes) or N (no): ")
                        if add_another_flight == "Y":
                            flights_list_done = False
                            break
                        elif add_another_flight == "N":
                            flights_list_done = True
                            break
                        else:
                            print("Invalid answer: Please type Y or N only.")

            print("\nFinally: ATTRACTIONS!")
            user_attractions_choice = input("If you want to skip this step, type SKIP and press 'Enter'. Otherwise, press 'Enter'. ")
            attractions_list_done = False

            if user_attractions_choice == "SKIP":
                attractions = []
            else:
                while not attractions_list_done:

                    attraction_name = input("Name of attraction: ")
                    attraction_address = input("Address of attraction: ")
                    attraction_summary = input("Short description of attraction: ")
                    attraction_tags = input("(Optional) Provide some tags that categorise what kind of activity this involves.\nExample of format required: hike, exciting, views\n")

                    attractions.append({
                        "attraction name": attraction_name,
                        "address": attraction_address,
                        "summary": attraction_summary,
                        "tag(s)": attraction_tags
                        })

                    while True:
                        add_another_attraction = input("Would you like to add another attraction? Type Y or N:")
                        if add_another_attraction == "Y":
                            attractions_list_done = False
                            break
                        elif add_another_attraction == "N":
                            attractions_list_done = True
                            break
                        else:
                            print("Invalid answer: Please type Y or N only.")

            add_itinerary(itineraries, name, location, description, start_date, end_date, flights, attractions)

        # Edit existing itinerary
        elif user_choice == "2":
            # Use rich module to print all the itineraries available, THEN pick module to pick an itinerary to modify
            print_table(itineraries)

            itinerary_prompt = 'Here are all the available itineraries. Which would you like to edit?:'
            itinerary_options = []
            for itinerary in itineraries:
                itinerary_options.append(itinerary["name"])
            itinerary_option, itinerary_index = pick(itinerary_options, itinerary_prompt)

            # Use pick module to select value to modify
            edit_prompt = 'Please select the item you want to edit: '
            edit_options = ['name', 'location', 'description', 'start_date', 'end_date', 'flights', 'attractions']
            edit_option, edit_index = pick(edit_options, edit_prompt)

            if edit_option == 'flights':
                attraction_choice = "N/A"
                flight_name_prompt = 'Which flight would you like to edit?'
                flight_name_options = []
                for itinerary in itineraries:
                    if itinerary["name"] == itinerary_option:
                        for flight in itinerary['flights']:
                            flight_name_options.append(flight["flight name"])
                flight_choice, flight_name_index = pick(flight_name_options, flight_name_prompt)
                flight_prompt = 'Finally, what about the flight would you like to edit?'
                flight_options = ['departure airport', 'departure date', 'arrival airport', 'arrival date']
                edit_option, flight_index = pick(flight_options, flight_prompt)
            elif edit_option == 'attractions':
                flight_choice = "N/A"
                attraction_name_prompt = 'Which attraction would you like to edit?'
                attractions_available = []
                for itinerary in itineraries:
                    if itinerary["name"] == itinerary_option:
                        for attraction in itinerary['attractions']:
                            attractions_available.append(attraction["attraction name"])
                attraction_choice, attraction_choice_index = pick(attractions_available, attraction_name_prompt)
                attractions_prompt = 'Which attraction property would you like to edit?'
                attraction_options = ['attraction name', 'address', 'summary', 'tag(s)']
                edit_option, attraction_index = pick(attraction_options, attractions_prompt)
            elif edit_option != 'flights' or edit_option != 'attractions':
                flight_choice = "N/A"
                attraction_choice = "N/A"
            
            # Set new value
            new_edit_value = input(f"What would you like to change {edit_option} to?\n(If a start/end date use DD-MM-YYYY format. If a flight date/time, use DD-MM-YYYY HH:MM)")

            edit_itinerary(itineraries, itinerary_option, edit_option, flight_choice, attraction_choice, new_edit_value)

        # Add flight or attraction to existing itinerary
        elif user_choice == "3":
            itinerary_prompt = 'Which itinerary would you like to add to?: '
            itinerary_options = []
            for itinerary in itineraries:
                itinerary_options.append(itinerary["name"])
            itinerary_option, itinerary_index = pick(itinerary_options, itinerary_prompt)

            edit_prompt = 'Please select which item you want to add: '
            edit_options = ['flights', 'attractions']
            option, edit_index = pick(edit_options, edit_prompt)

            # Add a flight
            if option == 'flights':
                flights = []
                flights_list_done = False
                while not flights_list_done:
                    departure_airport = input("Name of the airport you will depart from: ")
                    departure_date = input("Date & time of flight departure (Format: DD-MM-YYYY HH:MM): ")
                    arrival_airport = input("Name of the airport you will arrive at: ")
                    arrival_date = input("Date & time of flight arrival (Format: DD-MM-YYYY HH:MM): ")
                    flight_name = f"{departure_airport} to {arrival_airport}"
                    flights.append({
                        "flight name": flight_name,
                        "departure airport": departure_airport,
                        "departure date": departure_date,
                        "arrival airport": arrival_airport,
                        "arrival date": arrival_date
                    })
                    # Check if flight already exists
                    for itinerary in itineraries:
                        for flight in itinerary['flights']:
                            if flight_name == flight['flight name']:
                                print(f"Flight '{flight_name}' already exists!")
                                flights_list_done = True
                                break
                    if flights_list_done:
                        print("Returning to main menu...")
                        break

                    while True:
                        add_another_flight = input("Would you like to add another flight? Type Y (yes) or N (no): ")
                        if add_another_flight == "Y":
                            flights_list_done = False
                            break
                        elif add_another_flight == "N":
                            flights_list_done = True
                            break
                        else:
                            print("Invalid answer: Please type Y or N only.")
                add_new_flight(itineraries, itinerary_option, flights)

            # Add an attraction
            elif option == 'attractions':
                attractions = []
                attractions_list_done = False
                while not attractions_list_done:
                    attraction_name = input("Name of attraction: ")
                    attraction_address = input("Address of attraction: ")
                    attraction_summary = input("Short description of attraction: ")
                    attraction_tags = input(
                        "(Optional) Provide some tags that categorise what kind of activity this involves.\nExample of format required: hike, exciting, views\n")
                    attractions.append({
                        "attraction name": attraction_name,
                        "address": attraction_address,
                        "summary": attraction_summary,
                        "tag(s)": attraction_tags
                    })
                    # Check if attraction already exists
                    for itinerary in itineraries:
                        for attraction in itinerary['attractions']:
                            if attraction_name == attraction['attraction name']:
                                print(f"Attraction '{attraction_name}' already exists!")
                                attractions_list_done = True
                                break
                    if attractions_list_done:
                        print("Returning to main menu...")
                        break

                    while True:
                        add_another_attraction = input("Would you like to add another attraction? Type Y or N:")
                        if add_another_attraction == "Y":
                            attractions_list_done = False
                            break
                        elif add_another_attraction == "N":
                            attractions_list_done = True
                            break
                        else:
                            print("Invalid answer: Please type Y or N only.")
                add_new_attraction(itineraries, itinerary_option, attractions)

        # View itinerary
        elif user_choice == "4":
            if not itineraries:
                print("No itineraries available to view!")
            else:
                # Use pick module: Ask if they would like to view all itineraries, or a specific one
                view_prompt = 'Would you like to view all the existing itineraries?:  '
                view_options = ['View All', 'View One']
                option, index = pick(view_options, view_prompt)
                if option == 'View All':
                    print(f"\nFilter selected: {option}")
                    filter_option = "All"
                elif option == 'View One':
                    # Use pick module to select an itinerary by name and location
                    print(f"\nFilter selected: {option}")
                    itinerary_choice = 'Which itinerary would you like to view?: '
                    itinerary_options = []
                    for trip in itineraries:
                        itinerary_options.append(trip["name"])
                    filter_option, filter_index = pick(itinerary_options, itinerary_choice)
                view_itineraries(itineraries, filter_option)

        # Delete itinerary
        elif user_choice == "5":
            # Use pick to choose delete options
            delete_prompt = 'Would you like to delete a full itinerary, or a flight/attraction? \n(Note: You can only delete a flight or attraction if there is MORE THAN ONE available in the itinerary. \nIf there is only one, please select return.)'
            delete_options = ['Entire itinerary', 'Itinerary flight', 'Itinerary attraction', 'Return']
            delete_option, delete_index = pick(delete_options, delete_prompt)
            print_table(itineraries)

            if delete_option == 'Entire itinerary':
                itinerary_prompt = 'Which itinerary would you like to delete? '
                itinerary_options = []
                for itinerary in itineraries:
                    itinerary_options.append(itinerary["name"])
                itinerary_option, itinerary_index = pick(itinerary_options, itinerary_prompt)
                if delete_itinerary(itineraries, itinerary_option):
                    print("Itinerary has been deleted.")
                else:
                    print("Itinerary could not be found.")

            elif delete_option == 'Itinerary flight':
                while True:
                    multiple_flights = True
                    selected_type = "flights"
                    # Choose itinerary
                    itinerary_prompt = 'Which itinerary would you like to change? '
                    itinerary_options = []
                    for itinerary in itineraries:
                        itinerary_options.append(itinerary["name"])
                    itinerary_option, itinerary_index = pick(itinerary_options, itinerary_prompt)
                    # Choose flight
                    flight_prompt = 'Which flight would you like to delete? '
                    flight_options = []
                    for itinerary in itineraries:
                        if itinerary["name"] == itinerary_option:
                            if len(itinerary["flights"]) <= 1:
                                print("There is only one flight available, therefore you cannot delete it.")
                                multiple_flights = False
                                break
                            else:
                                for flight in itinerary["flights"]:
                                    flight_options.append(flight["flight name"])
                                    
                    # Checks if 'while True' statement should be broken
                    if not multiple_flights:
                        print("Returning to main menu...")
                        break
                    flight_id, itinerary_index = pick(flight_options, flight_prompt)

                    if delete_itinerary_item(itineraries, selected_type, itinerary_option, flight_id):
                        print(f"Flight '{flight_id}' has been deleted.")
                    else:
                        print("Flight could not be found.")
                    break

            elif delete_option == 'Itinerary attraction':
                while True:
                    multiple_attractions = True
                    selected_type = "attractions"
                    # Choose itinerary
                    itinerary_prompt = 'Which itinerary would you like to change? '
                    itinerary_options = []
                    for itinerary in itineraries:
                        itinerary_options.append(itinerary["name"])
                    itinerary_option, itinerary_index = pick(itinerary_options, itinerary_prompt)
                    # Choose attraction
                    attraction_prompt = 'Which attraction would you like to delete? '
                    attraction_options = []
                    for itinerary in itineraries:
                        if itinerary["name"] == itinerary_option:
                            if len(itinerary["attractions"]) <= 1:
                                print("There is only one attraction available, therefore you cannot delete it.")
                                multiple_attractions = False
                                break
                            else:
                                for attraction in itinerary["attractions"]:
                                    attraction_options.append(attraction["attraction name"])
                    # Checks if 'while True' statement should be broken
                    if not multiple_attractions:
                        print("Returning to main menu...")
                        break
                    attraction_id, itinerary_index = pick(attraction_options, attraction_prompt)

                    if delete_itinerary_item(itineraries, selected_type, itinerary_option, attraction_id):
                        print(f"Attraction '{attraction_id}' has been deleted.")
                    else:
                        print("Attraction could not be found.")
                    break

            elif delete_option == 'Return':
                print("Returning to previous menu...\n")

        # Log out
        elif user_choice == "6":
            app_running = False

    print("See you next time! 👋")


if __name__ == "__main__":
    run_app()
