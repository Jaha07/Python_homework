# Задача №9. Решение в группах
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# n = int(input("Enter n: "))
# count = 1
# total = 1
# while count <= n:
#     total *= count
#     count += 1
# print("Output =", total)

# n = int(input("Enter n: "))
# result = 1
# while n != 1:
#     result *= n
#     n -= 1
# print(result)



# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input("Enter N: "))
# fib1 = 0
# fib2 = 1
# count = 2
# while fib2 < n:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     count += 1
# if n == fib2:
#     print(count)
# else:
#     print(-1)



# Задача №13. Решение в группах
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2

# days = int(input("Enter amount of days: "))
# range(6) -> 0,1,2,3,4
# range(5,10) -> 5,6,7,8,9
# range(1, 10, 2) -> 1,3,5,7,9
# count_days = 0
# max_temp = 0
# for num_days in range(1, days + 1):
#     day = int(input(f"Enter temperature on {num_days}: "))
#     if day > 0:
#         count_days += 1
#     else:
#         if count_days > max_temp:
#             max_temp = count_days
#         count_days = 0
# print(max_temp)



# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# count_w = int(input("Enter amount of watermelons: "))
# min_w = int(input("Enter watermelon's weight"))
# max_w = min_w
# for i in range(count_w - 1):
#     w = int(input("Enter watermelon's weight"))
#     if w > max_w:
#         max_w = w
#     elif w < max_w:
#         min_w = w
# print(min_w, max_w)



# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# n = int(input("Enter amount of coins: "))
# count = 0
# for i in range(n):
#     side = int(input("Enter coin's side: "))
#     if side == 0:
#         count += 1
# print(count)

# Идеальное решение
# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)



# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# sum = int(input("Enter sum: "))
# multiply = int(input("Enter multi: "))
# c = 0
# for i in range(sum + multiply):
#     if c:
#         break
#     for j in range(sum + multiply):
#         if i + j == sum and i * j == multiply:
#             c = 1
#             print(*sorted([i, j]))
#             break

# Идеальное решение

# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)


# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8

# n = int(input())
# m = 1
# while m < n:
#     if(m < n):
#         if (m * 2 > n):
#             break
#         else:
#             m = m * 2
#             print(m)

# Идеальное решение

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1