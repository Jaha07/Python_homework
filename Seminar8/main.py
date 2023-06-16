# file_path = 'data.txt'
# with open(file_path, 'r+') as data_file:
#     data_file.write('\nnew!')

# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле. 
# 1. Программа должна выводить данные 
# 2. Программа должна сохранять данные в текстовом файле 
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека) 
# 4. Использование функций. Ваша программа не должна быть линейной

# def write_contacts(filename):
#     with open(filename, 'a', encoding='utf-8') as file:
#         file.write('\n' + input(f'Enter name and surname and phone number: '))
#     return file

# def read_contacts(filename):
#     contacts = []
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name' : name,
#                 'surname' : surname,
#                 'patronymic' : patronymic,
#                 'phone' : phone
#             }
#             print(name, surname, patronymic, phone)
#             contacts.append(contact)
#     return contacts

# filename = r'Seminar8\book.txt'
# a = int(input('1 - для ввода, 2 - для вывода \n'))
# if a == 1:
#     add_contact = write_contacts(filename)
# elif a == 2:
#     contact = read_contacts(filename)
#     # print('f{contact}')
# else:
#     print('No such function')


# HOMEWORK HOMEWORK HOMEWORK

# Задача 38:  Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.

# def write_contacts(filename):
#     with open(filename, 'a', encoding='utf-8') as file:
#         file.write('\n' + input(f'Enter name and surname and phone number: '))
#     return file

# def read_contacts(filename):
#     contacts = []
#     with open(filename, 'r') as file:
#         for line in file:
#             name, surname, patronymic, phone = line.strip().split(',')
#             contact = {
#                 'name' : name,
#                 'surname' : surname,
#                 'patronymic' : patronymic,
#                 'phone' : phone
#             }
#             print(name, surname, patronymic, phone)
#             contacts.append(contact)
#     return contacts

# filename = r'Seminar8\book.txt'
# a = int(input('1 - для ввода, 2 - для вывода \n'))
# if a == 1:
#     add_contact = write_contacts(filename)
# elif a == 2:
#     contact = read_contacts(filename)
#     # print('f{contact}')
# else:
#     print('No such function')

# def readfile(filename):
#     return open(filename).read().split('\n')

# def scan(data):
#     for i in data:
#         print(i)

# def search(data):
#     flag = 1
#     name = input('имя > ')
#     for line in data:
#         if name in line:
#             flag = 0
#             print(line)
#     if flag: print('no name given')

# data = readfile('book.txt')
# dict_command = {'1' : scan, '2' : search}

# print('Commands - 1,2,3,4,5')
# while True:
#     command = input('Command: > ')
#     if command in dict_command:
#         dict_command[command] (data)
#     else:
#         print('Command error!')

# в этой задаче я совсем запутался, не судите строго(