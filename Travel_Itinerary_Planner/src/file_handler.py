import os
import pickle
from pprint import pprint

ITINERARY_FILE = "itineraries.bin"
# Used \\ because of this warning: https://stackoverflow.com/questions/52335970/how-to-fix-syntaxwarning-invalid-escape-sequence-in-python
current_directory = f"{os.getcwd()}\\{ITINERARY_FILE}"
print(current_directory)


def load_itineraries():
    """
    Load tasks from a binary file using the pickle module.

    Returns:
        dictionary: A dictionary of Itinerary objects loaded from the binary file.
              If the file does not exist, an empty dictionary is returned.
    """
    if os.path.exists(current_directory):
        with open(ITINERARY_FILE, "rb") as file:
            return pickle.load(file)
    return []


def save_itineraries(itineraries):
    """
    Save a list of itineraries to a binary file using the pickle module.

    Args:
        itineraries (dict): A dictionary containing Itinerary objects to save.

    Side Effects:
        - Writes the serialized itinerary dictionary to ITINERARY_FILE.
        - Overwrites the file if it already exists.
    """
    with open(current_directory, "wb") as file:
        pickle.dump(itineraries, file)
