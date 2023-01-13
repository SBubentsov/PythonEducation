# 27. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# with open('input.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().split()
#     maxx = int(line[0])
#     minn = int(line[0])
#     for el in line:
#         if int(el) > maxx:
#             maxx = int(el)
#         elif int(el) < minn:
#             minn = int(el)
#     print(minn, maxx)

# 28. Найдите корни квадратного уравнения Ax^2 + Bx + C = 0 двумя способами:
# 1) с помощью математических формул

# with open('input.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().split()
#     a, b, c = int(line[0]), int(line[1]), int(line[2])
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         print('Корней нет')
#     elif d == 0:
#         print(-b / 2 * a)
#     else:
#         print((-b + d ** 0.5) / 2 * a)
#         print((-b - d ** 0.5) / 2 * a)

# 2) с помощью дополнительных библиотек Python
# pip install sympy

# a = 5
# b = 1
# c = 6
# import sympy
# x = sympy.Symbol('x')
# print(sympy.solve(f'{a}* x ** 2 + {b} * x + {c}'))

# 29. Задайте два числа. Напишите программу, которая найдет наименьшее общее кратное (НОК) этих двух чисел.

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# for i in range(a * b, 1, -1):
#     if i % a == 0 and i % b == 0:
#         nok = i
# print('НОК = ', nok)