# Посчитать сумму цифр любого целого или вещественного числа, число вводит пользователь. Через строку решать нельзя.
""""
number = float(input("Введите число: "))  # Вводим число как вещественное

# Извлекаем целую часть числа
integer_part = int(number)

# Извлекаем дробную часть числа
fractional_part = number - integer_part

# Инициализируем сумму цифр
sum_of_digits = 0

# Преобразуем целую часть в абсолютное значение, чтобы избежать проблемы с отрицательными числами
integer_part = abs(integer_part)

# Цикл для извлечения цифр целой части и их суммирования
while integer_part > 0:
    digit = integer_part % 10  # Извлекаем последнюю цифру целой части
    sum_of_digits += digit  # Суммируем цифру
    integer_part = integer_part // 10  # Убираем последнюю цифру из целой части

# Выводим сумму цифр
print("Сумма цифр целой части:", sum_of_digits)
print("Дробная часть числа:", fractional_part)
"""
from decimal import Decimal

number = Decimal(input("Введите число: "))  # Вводим число как Decimal

integer_part = int(number) # Извлекаем целую часть числа

fractional_part = number - Decimal(integer_part) # Извлекаем дробную часть числа

sum_of_digits = 0 # Инициализируем сумму цифр

integer_part = abs(integer_part) # Преобразуем целую часть в абсолютное значение, 
                                 # чтобы избежать проблемы с отрицательными числами

while integer_part > 0: # Цикл для извлечения цифр целой части и их суммирования
    digit = integer_part % 10  # Извлекаем последнюю цифру целой части
    sum_of_digits += digit  # Суммируем цифру
    integer_part = integer_part // 10  # Убираем последнюю цифру из целой части

temp_fractional_part = fractional_part # Цикл для извлечения цифр дробной части и их суммирования
while temp_fractional_part != 0:
    temp_fractional_part *= 10
    digit = int(temp_fractional_part)
    sum_of_digits += digit
    temp_fractional_part -= digit

print("Сумма цифр числа равна:", sum_of_digits) # Выводим сумму цифр целой части и дробной части


