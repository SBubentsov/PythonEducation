# 11. Напишите программу, которая принимает на вход число N и выдает последовательность из N членов
# пример: для N = 5: 1, -3, 9, -27, 81

# n = int(input('Введите натуральное значение N = '))
# print('Для N =', n, end= ': ')
# for i in range(n-1):
#     print((-3)**i, end= ', ')
# print((-3)**(n-1))

# 12. Для натурального N создать словарь индекс-значение, состоящий из элементов последовательности 3N+1.
# пример: для N = 6 {1:4, 2:7, 3:10, 4:13, 5:16, 6:19}

# n = int(input("Введите число: "))
# d = {i: 3*i + 1 for i in range(1, n+1)}
# print(f"Последовательность 3N+1 : {d}")

# 13. Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# str1 = input("Введите первую строку для проверки:")
# str2 = input("Введите вторую строку для поиска в первой строке:")

# count = 0
# k = 1
# for i in range(0, len(str1) - len(str2), k):
#     if str2 in str1[i:i+len(str2)]:
#         count += 1
#         k = len(str2)
#     else:
#         k = 1
# print(f"Вторая строка входит в первую {count} раз(а).")