"""
Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких 
собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста 
и с двух соседних с ним.

Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, 
находясь перед некоторым кустом заданной во входном файле грядки.
"""

import random, os
os.system('cls')

n = int(input("Введите количество кустов => "))
list_1 = [random.randint(0,10) for _ in range (n)]
print(*list_1, sep=", ")
max = 0

# 1.Решение через условия и поиск максимального значения в проверке этого условия (36 шага) - 
# скорость (0,0113) - 2 место (???)

for i in range(n):
    sum = list_1[i-1] + list_1[i] + list_1[(i+1)-n]
    if sum > max:
        max = sum
print(max)

# 2.Решение через условия и поиск максимального значения в проверке этого условия (34 шага) - 
# формула для суммы не унирвесальна...(скорость 0,0165)

# for i in range(n):
#     if i == 0 and ((list_1[n-1] + list_1[i] + list_1[i+1]) > max):
#         max = list_1[n-1] + list_1[i] + list_1[i+1]
#     elif i >=1 and i < n-1 and ((list_1[i-1] + list_1[i] + list_1[i+1]) > max):
#         max = list_1[i-1] + list_1[i] + list_1[i+1]
#     elif i == n-1 and ((list_1[i-1] + list_1[i] + list_1[0]) > max):
#         max = list_1[i-1] + list_1[i] + list_1[0]
# print(max)


# 3. Решение через дополнительный список с максимальными суммами (38 шагов) (скорость 0,0094)

# sum = list()
# for i in range(n):
#     if i == 0:
#         sum.append(list_1[n-1] + list_1[i] + list_1[i+1])
#     elif i >=1 and i < n-1:
#         sum.append(list_1[i-1] + list_1[i] + list_1[i+1])
#     elif i == n-1:
#         sum.append(list_1[i-1] + list_1[i] + list_1[0])
# print(*sum, sep=", ")
# sum.sort()
# print(f'Максимальное количество ягод с трёх соседних кустов = {sum[len(sum)-1]}')