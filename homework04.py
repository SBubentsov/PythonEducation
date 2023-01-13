# 30. Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# from math import pi

# d = int(input('Введите число для заданной точности числа Пи: '))
# print(f'число Пи с заданной точностью {d} равно {round(pi, d)}')

# 31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input('Введите число: '))
# i = 2  # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f'Простые множители числа {old} приведены в списке: {lst}')

# 32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# from random import randint
# n_list = list(randint(1,4) for i in range(randint(5,10+1)))
# print(n_list)
# n_mn = []
# for i in n_list:
#     if not i in n_mn:
#         n_mn.append(i)
# print(n_mn)    

# 33. НЕОБЯЗАТЕЛЬНАЯ Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint
# koef_max = 100
# k = int(input('Введите натуральную степень k: '))
# path = 'mn.txt'
# file = open(path,'w')
# for i in range(k,-1,-1):
#     koef = randint(0,koef_max)
#     if i == k:
#         while not koef:
#             koef = randint(0,koef_max)
#     if i != k and koef > 0:
#             file.write('+')
#     if koef != 0:
#         if koef != 1 or i == 0:
#             file.write(str(koef))
#             if i > 0:
#                 file.write('*')
#         if i>0:
#             file.write('x')
#         if i>1:
#             file.write('^'+str(i))
# file.write('=0')
# file.close

# 34. НЕОБЯЗАТЕЛЬНАЯ Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.