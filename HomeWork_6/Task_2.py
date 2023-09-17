# Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]
import random, os
os.system('cls')

min,max = int(input("Введите начальное значение = > ")), int(input("Введите конечное значение = > "))
rand_list = [random.randint(-10,10) for _ in range (random.randint(10,15))]
index_list = []
for i in range(len(rand_list)):
    if rand_list[i] >= min and rand_list[i] <= max:
        index_list.append(i)
print(*rand_list)
if len(index_list) == 0:
    print("Нет элементов, входящих в диапазон")
else:
    print(*index_list)