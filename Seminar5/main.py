# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., 
# где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21

# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
# print(fibonacci(7))



# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

# import random

# def create_journal(n):
#     journal_ = []
#     for i in range(n):
#         journal_.append(random.randint(1,5))
#     return journal_

# def change_min_max(number_list):
#     min_number = min(number_list)
#     max_number = max(number_list)
#     for i in range(len(number_list)):
#         if number_list[i] == max_number:
#             number_list[i] = min_number
#     return number_list

# n = int(input('Enter the amount of marks: '))
# test_list = create_journal(n)
# print(test_list)
# test_list = change_min_max(test_list)
# print(test_list)



# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)
# Input: 5 Output: yes

# def simple_num(num):
#     for i in range(2, num - 1):
#         if num % i == 0:
#             return False
#     return True

# print(simple_num(6))



# Задача №37. Решение в группах
# 15 минут
# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке. 
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
# Input:  2 -> 3 4 
# Output: 4 3

# def reverse_input(n):
#     if n == 1:
#         num = input('--> ')
#         return(num)
#     num = input('--> ')
#     return reverse_input(n - 1) + ' ' + num

# print(reverse_input(3))



# HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK HOMEWORK

# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵) 
# A = 2; B = 3 -> 8

# def expo(A, B):
#     if (B == 1):
#         return A
#     if (B != 1):
#         return (A * expo(A, B - 1))
    
# A = int(input('Enter A: '))
# B = int(input('Enter B: '))

# print('Result:', expo(A, B))



# Задача 28: Напишите рекурсивную функцию sum(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.
# 2 2 4

# def summa(a, b):
#     if a == 0:
#         return b
#     return summa (a - 1, b + 1)

# a = int(input('Enter a: '))
# b = int(input('Enter b: '))

# print('Result:', summa(a,b))



