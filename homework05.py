# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


# data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

# data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
# print(data)

# 39. (необязательная) Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

# b) Подумайте как наделить бота ""интеллектом""

# 40. (необязательная) Создайте программу для игры в ""Крестики-нолики"".

# import random
# from os import system, name  
 
# def clear():  
#     if name == 'nt':  
#         _ = system('cls')  
#     else:  
#         _ = system('clear')  

# def end(i):
#     if (i+1) % 3 == 0:
#         return '\n'
#     else:
#         return ''
        
# def printPole(lPole):
#     clear()  
#     for i in range(9):
#         if lPole[i] == 0:
#             print('_ ',end = end(i))
#         elif lPole[i] == 1:
#             print('X ', end = end(i))
#         else:
#             print('0 ', end = end(i))

# def isHorizontal(lPole):
#     bFlag = False
#     for i in range(3):
#         if lPole[i*3] != 0 and lPole[i*3] == lPole[i*3+1] and lPole[i*3+1] == lPole[i*3+2]:
#             bFlag = True
#     return  bFlag
# def isVertical(lPole):
#     bFlag = False
#     for i in range(3):
#         if lPole[i] != 0 and lPole[i] == lPole[i+3] and lPole[i+3] == lPole[i+6]:
#             bFlag = True
#     return  bFlag
# def isDiagonal(lPole):
#     bFlag = False
#     if lPole[4] != 0 and (lPole[0] == lPole[4] and lPole[4] == lPole[8] or lPole[2] == lPole[4] and lPole[4] == lPole[6]):
#         bFlag = True
#     return  bFlag

# def isWinner(lPole):
#     bFlag = False
#     if isHorizontal(lPole) or isVertical(lPole) or isDiagonal(lPole):
#         bFlag = True
#     return  bFlag


# lPole = [0,0,0,0,0,0,0,0,0]

# print('Игра "Крестики-нолики"')
# lNames=[]
# print()
# lNames.append(input('Введите имя первого игрока: '))
# lNames.append(input('Введите имя второго игрока: '))
# iActivPlayer = random.randint(0,1) 
# iLabel=1
# print('Случайно компьютер определил очередность ходов.')
# bFlagWin=True
# while bFlagWin:
#     print()
#     printPole(lPole)
#     print()
#     print(f'Ход игрока {lNames[iActivPlayer]}. ')
#     while True:
#         sMove = (input(f'{lNames[iActivPlayer]}, в какую ячейку хотите походить 1-9? '))
#         if sMove.isdigit():
#             iMove=int(sMove)
#             if iMove>=1 and iMove<=9 and lPole[iMove-1] == 0:
#                 break
#             else:
#                 print('Вы ввели неправильное число или поле занято.')
#     lPole[iMove-1] = iLabel
#     print()
#     printPole(lPole)
#     print()

#     if isWinner(lPole):
#         bFlagWin=False
#         print(f'{lNames[iActivPlayer]} выйграл(-а). Поздравляем победителя.')
#         print()
#     if not 0 in lPole:
#         print('Игроки сыграли вничью')  
#         print()
#         bFlagWin=False  
#     iActivPlayer = 1 - iActivPlayer
#     iLabel = 3 - iLabel

# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# sPathIn = 'TestRLE.txt'
# sPathOut = 'TestRLE.rle'

# fFileIn = open (sPathIn,'r')
# fFileOut = open (sPathOut,'w')
# sChar=''
# iCharCount=1
# bFlag = True
# while bFlag:
#     sCharRead = fFileIn.read(1)
#     if sCharRead == '':
#         bFlag = False
#     if sCharRead == sChar and iCharCount < 9:
#         iCharCount += 1
#     else:
#         if sChar != '':
#             fFileOut.write(sChar+str(iCharCount))
#         sChar = sCharRead
#         iCharCount = 1
# fFileIn.close
# fFileOut.close


# # unzip
# sPathIn = 'TestRLE.rle'
# sPathOut = 'TestRLE.out'

# fFileIn = open (sPathIn,'r')
# fFileOut = open (sPathOut,'w')
# bFlag = True
# while bFlag:
#     sCharRead = fFileIn.read(2)
#     if sCharRead == '':
#         bFlag = False
#     else:
#         fFileOut.write(sCharRead[0]*int(sCharRead[1]))
# fFileIn.close
# fFileOut.close

## Входные и выходные данные хранятся в отдельных текстовых файлах.