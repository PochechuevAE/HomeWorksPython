""" 
Три друга взяли вещи в поход. Сформируйте словарь, где ключ - имя друга, а значение - кортеж вещей. Ответьте на вопросы:
какие вещи взяли все три друга
какие вещи уникальны, есть только у одного друга
какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
Код должен расширяться на любое большее количество друзей.

hike = {
'Aaz': ("спички", "спальник", "дрова", "топор"),
'Skeeve': ("спальник", "спички", "вода", "еда"),
'Tananda': ("вода", "спички", "косметичка"),

"""

# Создаем словарь для хранения информации о друзьях и их вещах
hike = {}

# Запрашиваем у пользователя ввод количества друзей
num_friends = int(input("Введите количество друзей: "))

# Запрашиваем информацию о каждом друге
for i in range(num_friends):
    name = input(f"Введите имя друга {i + 1}: ")
    items = []

    # Запрашиваем вещи, которые взял друг
    while True:
        
        item = input(f"Введите вещь, которую взял {name} (или введите 'готово', чтобы закончить): ")    
        if item.lower() == "готово":               
            break
        elif not item:
            print("Ошибка: Некорректный ввод, повторите")        
            continue
        else:
            items.append(item)

    # Добавляем информацию о друге и его вещах в словарь
    hike[name] = items

# Все введенные данные находятся в словаре hike. Теперь можем анализировать их.
print()
# Находим вещи, которые взяли все друзья
common_items = set(hike[list(hike.keys())[0]])
for items in hike.values():
    common_items.intersection_update(items)

print("Вещи, которые взяли все друзья:", ", ".join(common_items) if common_items else "нет общих вещей")
print()
# Находим вещи, которые уникальны для каждого друга
unique_items = {}
for name, items in hike.items():
    items_set = set(items)
    for friend, friend_items in hike.items():
        if friend != name:
            items_set.difference_update(friend_items)
    unique_items[name] = items_set

for name, items in unique_items.items():
    print(f"Уникальные вещи для {name}: {', '.join(items)}" if items else f"{name} не взял уникальных вещей")
print()
# Находим вещи, которые есть у всех друзей, кроме одного, и имя друга, у которого этой вещи нет
for name, items in hike.items():
    others_have = set()
    for friend, friend_items in hike.items():
        if friend != name:
            others_have.update(friend_items)
    missing_items = others_have.difference(items)
    if missing_items:
        friend_without = [friend for friend, friend_items in hike.items() if missing_items.issubset(friend_items)]
        print(f"У {name} отсутствует(ют) вещи, которые есть у остальных {', '.join(friend_without)}: {', '.join(missing_items)}")

