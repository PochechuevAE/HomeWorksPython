""" 
Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
Фразы отделяются друг от друга пробелами.

Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки.
В ответе напишите "Парам пам-пам", если с ритмом все в порядке и "Пам парам", если с ритмом все не в порядке.
Если фраза только одна, то ритм определить не получится и необходимо вывести: "Количество фраз должно быть больше одной!".
"""

def check_rhythm(pooh_poetry):
    phrases = pooh_poetry.split()

    # Проверяем, что количество фраз больше одной
    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    # Функция для подсчета слогов (гласных) в слове
    def count_syllables(word):
        vowels = "уеыаоэяиюУЕЫАОЭЯИЮ"
        return sum(1 for char in word if char in vowels)

    # Получаем количество слогов в каждой фразе
    syllables_counts = [count_syllables(phrase.replace('-', '')) for phrase in phrases]

    # Проверяем, что количество слогов одинаковое в каждой фразе
    if all(count == syllables_counts[0] for count in syllables_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"

# Пример использования
stroka = "как ве-тер сме-ёт лис-ти"
result = check_rhythm(stroka)
print(result)
