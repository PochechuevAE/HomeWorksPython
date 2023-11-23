from easygui import *
from phone_book_funks import *

contacts = load_contacts()

msgbox("Вас приветствует Телефонный справочник")

while True:
    choices = ['Добавить контакт', 'Просмотреть все контакты', 
               'Изменить контакт','Поиск по фамилии', 'Удалить контакт','Выход']
    choice = buttonbox("Выберите действие", "Телефонный справочник", choices)

    if choice == 'Добавить контакт':
        msg = "Введите контакт"
        title = "Карточка контакта"
        field_names = ["Фамилия", "Имя", "Отчество", "Номер телефона"]
        field_values = multenterbox(msg, title, field_names)
        
        if field_values:
            add_contact(contacts, field_values)
            msgbox("Контакт успешно добавлен!")
    
    elif choice == 'Просмотреть все контакты':
        view_all_contacts(contacts)

    elif choice == 'Изменить контакт':
        if not contacts:
            msgbox("Справочник пуст. Нельзя изменить контакт.", 'Телефонный справочник')
        else:           
            if len(contacts) == 1:
                edit_contact(contacts, 0)
            else:
                try:
                    contact_names = [f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}" for contact in contacts]
                    choice = choicebox("Выберите контакт для изменения", "Телефонный справочник", contact_names)
                    if choice:
                        index = contact_names.index(choice)
                        edit_contact(contacts, index)
                except ValueError:
                    msgbox("Выбран неверный контакт. Изменение не выполнено.", 'Телефонный справочник')
                
    elif choice == 'Удалить контакт':
        if not contacts:
            msgbox("Справочник пуст. Нельзя удалить контакт.", 'Телефонный справочник')
        else:            
            if len(contacts) == 1:
                delete_contact(contacts, 0)
            else:
                try:   
                    contact_names = [f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}" for contact in contacts]
                    choice = choicebox("Выберите контакт для удаления", "Телефонный справочник", contact_names)

            
                    if choice:
                        index = contact_names.index(choice)
                        delete_contact(contacts, index)
                except ValueError:
                    msgbox("Выбран неверный контакт. Удаление не выполнено.", 'Телефонный справочник')
    
    elif choice == 'Поиск по фамилии':
        if not contacts:
            msgbox("Справочник пуст. Нечего искать.", 'Телефонный справочник')
        else:    
            surname_to_search = enterbox("Введите фамилию для поиска", "Поиск по фамилии")
            if surname_to_search:
                found_contacts = search_by_surname(contacts, surname_to_search)
                if found_contacts:
                    msg = ""
                    for contact in found_contacts:
                        msg += f"{contact['Фамилия']} {contact['Имя']} {contact['Отчество']}: {contact['Номер телефона']}\n"
                    msgbox(msg, 'Результат поиска')
                else:
                    msgbox(f"Контакт с фамилией '{surname_to_search}' не найден.", 'Результат поиска')          
              
    elif choice == 'Выход':
        msgbox("Всего хорошего, справочник закрыт!")
        break
