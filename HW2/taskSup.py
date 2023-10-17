""" 
Задача VERY HARD необязательная
Имеется список случайных целых чисел. Создайте список, в который попадают числа, описывающие максимальную сплошную возрастающую последовательность. Порядок элементов менять нельзя.
Одно число - это не последовательность.

Пример:

[1, 5, 2, 3, 4, 6, 1, 7] => [1, 7] так как здесь вразброс присутствуют все числа от 1 до 7

[1, 5, 2, 3, 4, 1, 7, 8 , 15 , 1 ] => [1, 5] так как здесь есть числа от 1 до 5 и эта последовательность длиннее чем от 7 до 8

[1, 5, 3, 4, 1, 7, 8 , 15 , 1 ] => [3, 5] так как здесь есть числа от 3 до 5 и эта последовательность длиннее чем от 7 до 8

"""
""" 
nums = [1, 5, 3, 4, 1, 7, 8 , 15 , 1 ]

curr = 1
count = 0
flag = 0

for _ in range(len(nums)):
    for i in nums:
        if i == curr:
            flag = 1
            count += 1
            curr += 1
            break
        print(f"i = {i}, count = {count} curr = {curr} ")
    if flag = 0
"""
numbers = [1, 5, 3, 4, 1, 7, 8, 15, 1]

max_seq = []
current_seq = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_seq.append(numbers[i])
    else:
        if len(current_seq) > len(max_seq):
            max_seq = current_seq
        current_seq = [numbers[i]]

if len(current_seq) > len(max_seq):
    max_seq = current_seq

print(max_seq)








