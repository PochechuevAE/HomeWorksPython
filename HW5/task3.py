""" 
Напишите рекурсивную программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный.

*Пример:* 

2+2 => 4; 

1+2*3 => 7; 

1-2*3 => -5;

- Добавьте возможность использования скобок, меняющих приоритет операций.

    *Пример:* 


    1+2*3 => 7; 

    (1+2)*3 => 9;
    
Тут может помочь библиотека re

"""

def evaluate(expression):
    # Шаг 1: Удалить пробелы из выражения
    expression = expression.replace(" ", "")
    
    # Шаг 2: Разделить выражение на токены
    tokens = []
    i = 0
    while i < len(expression):
        if expression[i] in "+-*/":
            tokens.append(expression[i])  # Оператор
            i += 1
        else:
            num = ""
            while i < len(expression) and expression[i].isdigit():
                num += expression[i]
                i += 1
            tokens.append(num)  # Число

    # Теперь в списке tokens у нас есть числа и операторы разделенные в правильном порядке
    return tokens

# Тестирование


def find_first_tasks(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '*':
            # Вычисляем результат операции и заменяем элементы в списке
            result = int(tokens[i - 1]) * int(tokens[i + 1])
            tokens[i-1:i+2] = [result]
            # Рекурсивно вызываем функцию, чтобы продолжить вычисления
            find_first_tasks(tokens)
        elif tokens[i] == '/':
            result = int(tokens[i - 1]) // int(tokens[i + 1])
            tokens[i-1:i+2] = [result]
            find_first_tasks(tokens)
        else:
            i += 1

def find_second_tasks(tokens):
    i = 0
    while i < len(tokens):
        if tokens[i] == '+':
            # Вычисляем результат операции и заменяем элементы в списке
            result = int(tokens[i - 1]) + int(tokens[i + 1])
            tokens[i-1:i+2] = [result]
            # Рекурсивно вызываем функцию, чтобы продолжить вычисления
            find_second_tasks(tokens)
        elif tokens[i] == '-':
            result = int(tokens[i - 1]) - int(tokens[i + 1])
            tokens[i-1:i+2] = [result]
            find_second_tasks(tokens)
        else:
            i += 1
            

# Тестирование
#tokens = ["2", "+", "3", "*", "5", "-", "4"]
expression = input("Введите выражение: ")
tokens = evaluate(expression)
print(tokens)
find_first_tasks(tokens)
find_second_tasks(tokens)
print(tokens[0])

