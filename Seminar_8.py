# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать
#  функционал
# для изменения и удаления данных.


# 1.Создание файла:+++
#     - открываем файл на дозапись #a +++
# 2.Добавление контакта
#     - запросить у пользователя новый контакта
#     - открыть файл на дозапись #a
#     - добавить новый контакт
# 3.Вывод данных на экран:
#     -открыть файл на чтение #r
#     - считать файл
#     - вывести на экран
# 4.Поиск контакта:
#     - выбор варианта поиска
#     - запросить данные для поиска
#     - открыть файл на чтение
#     - считываем данные, сохранить их в переменную
#     - осуществляем поиск контакта
#     - вывести на экран
# 5. Создание UI:
#     - вывести меню на экран +++
#     - запросить у пользователя вариант действия +++
#     - запустить соответствующую функцию 
#     - осуществить возможность выхода из программы



def input_surname():
    return input('Введите фамилию контакта: ')

def input_name():
    return input('Введите имя контакта: ')

def input_patronymic():
    return input('Введите отчество контакта: ')

def input_phone():
    return input('Введите номер контакта: ')

def input_address():
    return input('Введите город контакта: ')

def create_contact():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    return f'{surname} {name} {patronymic}: {phone}\n{address}\n\n'
    

def add_contact():
    contact_str = create_contact()
    with open("phonebook.txt", 'a', encoding='UTF-8') as file:
        file.write(contact_str)


def print_contacts():
    with open("phonebook.txt", 'r', encoding='UTF-8') as file:
        print(file.read())

def search_contacts():
    pass


def interface():
    with open("phonebook.txt", "a", encoding='UTF-8'):
        pass


var = 0
while var != '4':
    print(
        'Возможные варианты:\n'
        '1. Добавить контакт\n'
        '2. Вывести на экран\n'
        '3. Поиск контакта\n'
        '4. Выход'
        )
    var = input('Выберите вариант действия: ')
    while var not in ('1', '2', '2', '4'):
        print('Неккоректный ввод: ')
        var = input('Выберите вариант действия: ')

    match var:
        case '1':
            add_contact()
        case '2':
            print_contacts() 
        case '3':
            search_contacts()  
        case '4':
            print('Пока')



if __name__ == '_main__':
    interface()

