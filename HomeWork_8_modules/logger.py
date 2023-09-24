from data_create import *

def enter_data():
    name = enter_first_name()
    surname = enter_midle_name()
    family = enter_last_name()
    number = enter_phone_number()
    address = enter_address()
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} {surname} {family} {number} {address}\n\n')

def print_customer(to_print):
    print('')
    new_customer = to_print.rsplit(' ',2)
    for elem in new_customer:
        print(f'{elem}')
    print('')
            
def print_data():
     with open('phone_book.txt', 'r', encoding='utf-8') as file:
        to_print = file.read().strip().split('\n\n')
        for customer in to_print:
            print_customer(customer)
            
def create_request(request:str) -> int:
    print(f'{request}:\n'
        '1. Имя\n'
        '2. Отчество\n'
        '3. Фамилия\n'
        '4. Номер\n'
        '5. Адрес\n')
    index = int(input('Введите индекс: '))
    while index not in range(1,6):
        print('\nНекоректный ввод\n')
        index = int(input('Введите индекс: '))
    return index -1
        
def search_data():
    index = create_request('Выберите вариант поиска')
    searched = input('Введите данные для поиска: ').title()
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
        flag = True
        for item in data:
            new_item = item.split()
            if searched == new_item[index]:
                print_customer(item)
                flag = False
        if flag: print(f'\nИнформация не найдена\n')
                
def change_data():
    to_search = input('Введите имя или фамилию абонента: ').title()
    index = create_request('Выберите что вы хотите изменить')
    new_info = str(input('Введите новые данные: '))
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        flag = True
        for item in data:
            new_item = item.split()
            if to_search == new_item[0] or to_search == new_item[2]:
                new_item[index] = new_info
                print_customer(' '.join(new_item))
                flag = False
            item = ' '.join(new_item)
            file.write(f'{item}\n\n')
        if flag: print(f'\nИнформация не найдена\n')
        
def delete_data():
    to_search = input('Введите имя или фамилию абонента: ').title()
    print('Вы хотите удалить всю информацию об абоненте? \n'
        '1. Да\n'
        '2. Нет\n')
    choose = int(input('=> '))
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        data = file.read().strip().split('\n\n')
    with open('phone_book.txt', 'w', encoding='utf-8') as file:
        if choose == 1:
            flag = True
            for item in data:
                new_item = item.split()
                if to_search == new_item[0] or to_search == new_item[2]:
                    flag = False
                else:
                    item = ' '.join(new_item)
                    file.write(f'{item}\n\n')
            if flag: print(f'\nИнформация не найдена\n')
            
        if choose == 2:
            index = create_request('Выберите что вы хотите удалить')
            flag = True
            for item in data:
                new_item = item.split()
                if to_search == new_item[0] or to_search == new_item[2]:
                    new_item[index] = '-----'
                    print_customer(' '.join(new_item))
                    flag = False
                item = ' '.join(new_item)
                file.write(f'{item}\n\n')
            if flag: print(f'\nИнформация не найдена\n')  
