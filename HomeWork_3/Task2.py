'''
Задача 2

Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5
'''
import random, os
os.system('cls')

n,k = int(input('Введите кол-во элементов = > ')), int(input('Введите число к которому нужно найти ближайшее по значению в списке = > '))

list_1 = [random.randint(0, 10) for _ in range (n)]

print(*list_1, sep=", ")


min_diff = abs(k - list_1[0])
num = list_1[0]
num_2 = list_1[0]

for i in list_1:
    if abs(k - i) < min_diff:
        min_diff = abs(k-i)
        num = i
    elif abs(k - i) == min_diff and abs(k - i) != num:
        num_2 = i
if abs(num_2 - k) == abs(num - k) and num_2 != num:
    print(f'Ближайшие числа в списке: {num} и {num_2}')
else:
    print(num)

'''
# Решение с сайта5

m = abs(k - list_1[0])  # модуль числа
number = list_1[0]
for i in range(1, len(list_1)):
    if m > abs(list_1[i] - k):
        m = abs(list_1[i] - k)
        number = list_1[i]
print(number)
'''