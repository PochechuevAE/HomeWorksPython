import json
from easygui import *

def load_contacts():
    try:
        with open("phone_book.json", "r") as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []