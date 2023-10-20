""" 
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [1, 2, 3, 4, 5]
k = 6
# 5


"""

list_1 = [1, 2, 3, 4, 5]
k = 5

# for index in range(len(list_1)):
#     if list_1[index] <= k + 1 and list_1[index] >= k - 1:
#         print(list_1[index])
#     else:
#         continue

serchmin = min(list_1, key=lambda x: abs(x - k))
print(serchmin)

list_1 = [1, 2, 3, 4, 5]
k = 6

closest = None
min_difference = float('inf')

for number in list_1:
    difference = abs(number - k)
    if difference < min_difference:
        min_difference = difference
        closest = number

print(closest)
