'''
Задача 10
На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
Выведите минимальное количество монет, которые нужно перевернуть
Пример:
5 -> 1 0 1 1 0
2
'''

import random, os
os.system('cls')

n = int(input('Введите количесвто монеток на столе = > '))
heads = 0
tails = 0
array = [n]

for i in range (n):
    array = [random.randint(0, 1) for _ in range (n)]

print(*array, sep = ", ")

for i in range (n):
    if array [i] == 1:
        heads = heads + 1
    else:
        tails = tails + 1

print("Минимальное число монеток, которые нужно перевернуть:")
print (tails) if tails <= heads else print (heads)


