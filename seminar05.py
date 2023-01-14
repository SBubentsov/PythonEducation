# 35. В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

# with open('input.txt', 'r', encoding='utf-8') as file:
# line = file.readline().split()
# some_list = [1,2,3,4,6,7,8,9]
# print(some_list)
# for i in range(1, len(some_list)):
#     if some_list[i] -1 !=  some_list[i-1]:
#         print(some_list[i]-1)


# 36. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. Порядок элементов менять нельзя.
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] ⇒ [1,5] и [2,3,4,6] и [1,7]

# import random
# some_list = [random.randint(1, 10) for i in range(10)]
# print(some_list)
# some_list.append(0)
# ind = 0
# res_list = []
# temp_list = []
# while ind < len(some_list) - 1:
#     if some_list[ind] < some_list[ind + 1]:
#         temp_list.append(some_list[ind])
#     else:
#         if len(temp_list) != 0:
#             temp_list.append(some_list[ind])
#             res_list.append(temp_list)
#             temp_list = []
#     ind += 1
# print(res_list)



# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".