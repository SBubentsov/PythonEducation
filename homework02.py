# 14. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# from decimal import Decimal
# sum_digits = 0
# num_dec = Decimal(input('Введите число: '))
# if num_dec < 0:
#     num_dec *= -1
# while num_dec % 1 > 0: 
#     num_dec *=10
# while num_dec > 0:
#     sum_digits = sum_digits + int(num_dec % 10)
#     num_dec //= 10
# print(sum_digits)

# 15. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите натуральное N: '))
# current_product = 1
# for n in range(1, N+1):
#     current_product *= n
#     print(current_product, end=' ')

# 16. Задайте список из n чисел последовательности (1 + 1/n) ** n и выведите на экран их сумму.
# Пример:
# -Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06

# N = int(input('Введите натуральное N: '))
# func = {}
# sum_func = 0
# for n in range(1, N+1):
#     func[n] = round((1+1/n)**n, 2)
#     sum_func += func[n]
# print(func)
# print('sum = ', sum_func)

# 18. Реализуйте алгоритм перемешивания списка.

# import random

# N = int(input('Введите число N: '))
# spisok = list(range(1, N+1))
# print('Начальный список   : ', spisok)
# sorted = [0]*len(spisok)
# index_temp = random.randint(0, N-1)
# sorted[index_temp] = 1
# temp = spisok[index_temp]
# for i in range(len(spisok)-1):
#     index_temp1 = random.randint(0, N-1)
#     while sorted[index_temp1]:
#         index_temp1 += 1
#         if index_temp1 == N:
#             index_temp1 = 0
#     spisok[index_temp] = spisok[index_temp1]
#     sorted[index_temp1] = 1
#     index_temp = index_temp1
# spisok[index_temp] = temp
# print('Cписок перемешанный: ', spisok)