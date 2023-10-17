""" 
Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

"""

# n = int(input("Введите число N: "))
# k = 1
# step = 2

# while step < n:
#     step = k * 2
#     k += 1
#     if k % 2 == 0:
#         print(step)

N = 16  # Замените на ваше число N
power_of_two = 1

while power_of_two <= N:
    print(power_of_two)
    power_of_two *= 2