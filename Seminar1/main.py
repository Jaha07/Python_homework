# Задача №1. Решение в группах
# Семинар 1. Ввод-вывод, операторы ветвления
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

# print("Enter n number: ")
# n = int(input())
# print("Enter m number: ")
# m = int(input())
# result = (m / n)
# ostatok = (m % n)
# if (ostatok > 0):
#     result = result + 1
# print(int(result))



# Задача №3. Решение в группах
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# a = int(input("Enter number a: "))
# b = int(input("Enter number b: "))
# c = int(input("Enter number c: "))
# class_A = a // 2 + a % 2
# class_B = b // 2 + b % 2
# class_C = c // 2 + c % 2
# total = class_A + class_B + class_C
# print("Total =", total)



# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

# num = int(input("Enter your number: "))
# if ((num % 4 == 0) and (num % 100 != 0)) or (num % 400 == 0):
#     print("Yes")
# else:
#     print("No")

#  HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK

# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# result = a + b + c
# print("resutl = ", result)



# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# sum = int(input("Enter sum: "))
# sp = 0
# sp = sum / 3
# katya = sp * 2
# petya = sp / 2
# segrey = sp / 2
# print(f"Katya = {katya}, Petya = {petya}, Sergey = {segrey}")



# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# ticket = int(input("Enter the number: "))
# a = ticket // 100000
# b = int(ticket % 100000 / 10000)
# c = int(ticket % 10000 / 1000)
# d = int(ticket % 1000 / 100)
# e = int(ticket % 100 / 10)
# f = int(ticket % 10)
# if (a + b + c == d + e + f):
#     print("Yes")
# else:
#     print("No")



# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no



# n = int(input())
# m = int(input())
# k = int(input())
# if k < n * m and ((k % n == 0) or (k % m == 0)):
#     print('YES')
# else:
#     print('NO')






