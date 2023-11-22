import json
from easygui import *

def load_contacts():
    try:
        with open("phone_book.json", "r") as file:
            contacts = json.load(file)
        return contacts
    except FileNotFoundError:
        return []
    
def save_contacts(contacts):
    with open("phone_book.json", "w") as file:
        json.dump(contacts, file, indent=2)

def add_contact(contacts, data):
    contacts.append({"Фамилия": data[0], "Имя": data[1], "Отчество": data[2], "Номер телефона": data[3]})
    save_contacts(contacts)