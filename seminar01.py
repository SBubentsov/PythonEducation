# Семинар 1.

#   1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
#     *Примеры:* 
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# a = int(input('a ='))
# b = int(input('b ='))

# if a**2 == b or b**2 == a:
#     print('да')
# else :
#     print('нет')



#   2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# some_list = []
# for _ in range(5):
#     x = int(input())
#     some_list.append(x)
# # print(max(some_list))
# maxel = some_list[0]
# for el in some_list:
#     if el > maxel:
#         maxel = el
# print(maxel)

# maxel = int(input())
# for _ in range(4):
#     x = int(input())
#     if x > maxel:
#         maxel = x
# print(maxel)

#   3. Напишите программу, которая будет принимать на вход число N, и выводить числа от -N до N.

# N = int(input())
# for i in range(-N, N):
#     print(i, end=', ')
# print(N)

# N = int(input())
# print(*range(-N, N + 1), sep=', ')

# N = int(input())
# some_list = []
# for i in range(-N, N + 1):
#     some_list.append(i)
# print(*some_list, sep=', ')

#   4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

# a = float(input())
# if a % 1 == 0:
#     print('нет')
# else:
#     print(int(a * 10) % 10)

# a = input()
# if '.' in a:
#     ind = a.index('.')
#     print(a[ind + 1])
# else:
#     print('нет')

#   5. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

# a = int(input())
# if (a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0:
#     print('да')
# else:
#     print('нет')

# a = int(input())
# print((a % 5 == 0 and a % 10 == 0 or a % 15 == 0) and a % 30 != 0)