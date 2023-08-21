"""
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.
Пример:
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)
"""

n = int(input('Insert 3-digits number => '))
res = n//100 + (n % 100)//10 + n % 10
print(f'Sum of digits of the number n = {n} -> res = {res}')