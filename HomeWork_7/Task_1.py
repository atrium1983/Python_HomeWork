# Задача 34:  
# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, 
# насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов 
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, 
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  
import os
os.system('cls')

def check_poem(poem):
    vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
    count = 0
    for phrase in poem:
        count_temp = 0
        for letter in phrase:
            if letter in vowels:
                count_temp += 1
        if count == 0:
            count = count_temp
        if count_temp != count:
            return 'Пам парам'
    return 'Парам пам-пам'

poem = str(input("Введите текст стихотворения = > ")).split()
print(check_poem(poem))
    
# Решение препода:

def sum_vowels(phrase):
    vowels_letter = 'аоэеиыуёюя'
    k = 0
    for letter in phrase:
        if letter in vowels_letter:
            k += 1
    return k

def pam_param(phrases):
    sum_0 = sum_vowels(phrases[0])
    for phrase_i in phrases[1:]:
        sum_i = sum_vowels(phrase_i)
        if sum_0 != sum_i:
            return 'Пам парам'
    return 'Парам пам-пам'

text = input("Введите текст песни Винни-Пуха:").split()
print(pam_param(text))
    