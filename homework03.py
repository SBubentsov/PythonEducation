# 22. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def sum_odd_index(lst):
#     s = 0
#     for i in range(len(lst)):
#         if i % 2 != 0:
#             s += lst[i]
#     print('Сумма элементов на нечетных позициях равна: ', s)

# num_list = list(map(int, input('Введите числа через пробел: ').split()))
# sum_odd_index(num_list)

# 23. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# def mult_lst(lst):
#     l = len(lst)//2 + 1 if len(lst) % 2 != 0 else len(lst)//2
#     new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
#     print('Произведение пар чисел списка: ', new_lst)

# num_list = list(map(int, input('Введите числа через пробел: ').split()))
# mult_lst(num_list)

# 24. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input('Введите числа через пробел:').split()))
# new_lst = [round(i % 1, 2) for i in lst if i % 1 != 0]
# print("{:.2f}".format(max(new_lst) - min(new_lst)))

# 25. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# s = ''
# n = int(input('Введите число для преобразовывания десятичного числа в двоичное: '))
# while n != 0:
#     s = str(n % 2) + s
#     n //= 2
# print(s)

# 26. НЕОБЯЗАТЕЛЬНАЯ Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]