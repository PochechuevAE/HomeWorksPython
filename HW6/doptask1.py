""" 
Задача НЕГАФИБОНАЧЧИ по желанию
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

Пример:

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

"""

import random

k = random.randint(5, 10)

def fibonacci(k):
    a, b = 1, 1
    for i in range(k):
        yield a
        a, b = b, a + b

data1 = list(fibonacci(k))
data2 = [0]
data3 = data2 + data1
data4 = []
for i in range(len(data3)):
    if i % 2 == 0:
        data4.append(-data3[i])
    else:
        data4.append(data3[i])
data4.reverse()

itogData = data4 + data3[1:]
print()
print(itogData)


