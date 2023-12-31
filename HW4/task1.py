""" 
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
На вход подается 2 числа через пробел: n m
n - кол-во элементов первого множества.
m - кол-во элементов второго множества.
Затем подаются элементы каждого множества через пробел в виде строки. ! Писать input() не надо

Пример

На входе:


var1 = '5 4' # количество элементов первого и второго множества
var2 = '1 3 5 7 9' # элементы первого множества через пробел
var3 = '2 3 4 5' # элементы второго множества через пробел

"""
var1 = '5 4'
var2 = '1 3 5 7 9'
var3 = '2 3 4 5'

# Разбиваем строку на части и преобразуем в целые числа
n, m = map(int, var1.split())
set1 = set(map(int, var2.split()))
set2 = set(map(int, var3.split()))

# Находим пересечение множеств и сортируем результат
intersection = sorted(set1.intersection(set2))

# Выводим результат
result = ' '.join(map(str, intersection))
print(result)
