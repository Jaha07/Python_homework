# lst = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(lst)))

# my_set = {1, 1, 2, 4, 'Hello, world!'}
# print(my_set)

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# lst = [1, 2, 3, 4, 5]
# k = 3
# for i in range(k):
#     num = lst.pop(-1)
#     lst.insert(0, num)
# print(lst)



# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# start_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII":"S007"}]

# val_list = []
# for little_dict in start_list:
#     for val in little_dict.values():
#        val_list.append(val)
# print(set(val_list))

# HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1

# N = abs(int(input("Enter the amount of numbers: ")))
# A_entered = input("Enter your numbers: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N:
#     print("The entered data is wrong!")
# else:
#     X = int(input("Enter X number: "))
#     count = 0
#     for i in range(N):
#         if A_num[i] == X:
#             count += 1
#     print(f"The number {X} is mentioned {count} time(s)")



# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5

# N = abs(int(input("Enter the amount of numbers: ")))
# A_entered = input("Enter numbers: ").split()
# A_num = list(map(int, A_entered))
# if len(A_num) != N or N == 0:
#     print("The entered data is wrong!")
# else:
#     X = int(input("Enter X: "))
#     min = abs(X - A_num[0])
#     index = 0
#     for i in range(1, N):
#         count = abs(X - A_num[i])
#         if count < min:
#             min = count
#             index = i
#     print(f"{A_num[index]} is close to {X}.")



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность. В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо
# только английские, либо только русские буквы.

# Ввод:
# ноутбук
# Вывод:
# 12



# eng = {1:'AEIOULNSTR',
#       	2:'DG',
#       	3:'BCMP',
#       	4:'FHVWY',
#       	5:'K',
#       	8:'JZ',
#       	10:'QZ'}
# rus = {1:'АВЕИНОРСТ',
#       	2:'ДКЛМПУ',
#       	3:'БГЁЬЯ',
#       	4:'ЙЫ',
#       	5:'ЖЗХЦЧ',
#       	8:'ШЭЮ',
#       	10:'ФЩЪ'}
# N = abs(int(input("Enter 1 for ENGLISH, or 0 for RUSSIAN: ")))
# word = input("What is your word: ").upper()
# if N == 1:
# 	print("Result:", sum([k for i in word for k, v in eng.items() if i in v]), "points")
# elif N == 0:
# 	print("Result:", sum([k for i in word for k, v in rus.items() if i in v]), "points")
# else:
#     print("Error!")

