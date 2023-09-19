# Задача 30:  
# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
import os
os.system('cls')

def arithmetic_progression (first_element, difference, quantity):
    arith_list = []
    for i in range(quantity):
        arith_list.append(first_element + i * difference)
    return arith_list

a_1 = int(input("Введите первый элемент арифметической прогрессии = > "))
d = int(input("Введите разность = > "))
n = int(input("Введите количество элементов = > "))

print(f'Первый элемент арифметической прогрессии = {a_1}, разность = {d}, количество элементов = {n}\nМассив элементов арифметической прогрессии = > {arithmetic_progression(a_1,d,n)}')
print(list(range(a_1, a_1 + d * n , d))) #совет преподавателя