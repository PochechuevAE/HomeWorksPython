from easygui import *
from phone_book_funks import *

contacts = load_contacts()

msgbox("Вас приветствует Телефонный справочник")

while True:
    choices = ['Добавить контакт', 'Просмотреть все контакты', 
               'Изменить контакт', 'Удалить контакт','Выход']
    choice = buttonbox("Выберите действие", "Телефонный справочник", choices)

    if choice == 'Добавить контакт':
        msg = "Введите контакт"
        title = "Карточка контакта"
        field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
        field_values = multenterbox(msg, title, field_names)
        
        if field_values:
            add_contact(contacts, field_values)
            msgbox("Контакт успешно добавлен!")
