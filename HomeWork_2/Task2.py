'''
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3
'''
import math, os
os.system('cls')

x = 0
y = 0
summa = int(input('Сумма двух натуральных чисел = '))
product = int(input('Произведение двух натуральных чисел = '))
# решение задачи сводиться к решению квадратных уравнений x*x -summa*x + product = 0, y*y - summa*y + product = 0
"""
d = (-summa)*(-summa) - 4 * product     # для решения потребуется дискриминант

if d >= 0:                   # если d = 0, то x = y, если d > 0, x =! y. При отрицательном значении решения нет
    x = int ((summa - math.sqrt(d)) / 2)
    y = int ((summa + math.sqrt(d)) / 2)
    print(f"Задуманные числа : {x} и {y}")
else:
    print("Для введенных значений нет решений")
"""
for x in range (product):
    for y in range (product):
        if x + y == summa and x*y == product:
            print(f"Задуманные числа : {x} и {y}")
        y = y + 1
    x = x + 1