'''
Задача 1

Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
Пример:
list_1 = [1, 2, 3, 4, 5]
k = 3
# 1
'''

import random, os
os.system('cls')

n,k = int(input('Введите кол-во элементов в списке = > ')), int(input('Введите число которое нужно найти = > '))

#list_1 = []
#for i in range (n):
#    list_1.append(random.randint(0, 10))

list_1 = [random.randint(0, 10) for _ in range (n)]

print(*list_1, sep=", ")
num = 0

for i in list_1:
    if i == k:
        num = num +1

print(f'Число {k} в списке встречается {num} раз(а)')