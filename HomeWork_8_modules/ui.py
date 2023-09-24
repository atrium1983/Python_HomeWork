from logger import *

def user_interface():
    cmd = 0
    while cmd != '6':
        print('Выберите действие:\n'
            '1. Добавить контакт\n'
            '2. Вывести все контакты\n'
            '3. Поиск\n'
            '4. Внести изменения\n'
            '5. Удалить данные абонента\n'
            '6. Выход\n')
        cmd = input('Введите индекс: ')
        while cmd not in ('1','2','3','4','5','6'):
            print('Некоректный ввод')
            cmd = input('Введите индекс: ')
            
        match cmd:
            case '1': 
                enter_data()
            case '2':
                print_data()
            case '3':
                search_data()
            case '4':
                change_data()
            case '5':    
                delete_data()
            case '6':    
                print('Всего доброго!')