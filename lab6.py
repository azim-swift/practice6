"""Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение на характеристики объектов (которое будет сокращать количество переборов)  и целевую функцию для нахождения оптимального  решения."""
"""Вариант 7. Вывести все натуральные числа до n, в записи которых встречается ровно одна нечетная цифра."""


import time
import itertools as it
import copy as c

"""СУТЬ АЛГОРИТМА ЗАКЛЮЧАЕТСЯ В ТОМ ЧТО МЫ БЕРЕМ ПАРУ ЧИСЛЕМ ИЗ ИСХОДНОЙ МАТРИЦЫ И ОТНОСИТЕЛЬНО НЕЕ МЕНЯЕМ ДРУГИЕ ПАРЫ
ЗАТЕМ ОБНОВЛЯЕМ РАБОЧУЮЮ МАТРИЦУ И ПОВТОРЯЕМ ЦИКЛ ДЛЯ СЛЕДУЮЩЕЙ ПАРЫ"""


"""ПЕРЕМEННЫЕ"""

n = int(input("Введите число для квадратной матрицы "))
matrix_ORIGINAL = [[  (j+1)*(i+1)  for j in range(0,n)] for i in range(n)]# СОЗДАЕМ МАТРИЦУ
matrix = c.deepcopy(matrix_ORIGINAL)# КОПИРУЕМ МАТРИЦУ ДЛЯ РАБОТЫ С НЕЙ
minus = n-1 #определяет индекс для элемента побочной диагонали
main_line = [ matrix_ORIGINAL[i][i] for i in range(n)]#СОЗДАЕМ СПИСОК ИЗ ГЛАВНОЙ ДИАГОНАЛИ
second_line = []
"""СОЗДАЕМ СПИСОК ИЗ ПОБОЧНОЙ ДИАГОНАЛИ"""
for i in range(0,n):

    second_line.append(matrix_ORIGINAL[i][minus])
    minus -=1

minus = n - 1 #снова присваиваем значение
flag = 0 #отвечает за ведущую строку в комбинации
save = 0 #спомогательная переменная

choose=int(input("0 - простая / 1 - сложная "))
print("исходная матрица ")
print('\n'.join('\t'.join(map(str, row)) for row in matrix))

"""-------------------------------------"""
"""С ПОМОЩЬЮ СТАНДАРТНЫХ ФУНКЦИЙ ПИТОН  """
"""-------------------------------------"""
if choose == 0:
    print('\n',"начало работы программы по стандарту")


    while flag < n: #ИДЕМ ДО ТЕХ ПОР ПОКА НЕ ПРОЙДЕМ ПО ВСЕМ ПАРАМ
        print ("введущая пара ", matrix[flag][flag],matrix[flag][minus-flag])
        for i in range (0,n):

             if i == flag:#ЕСЛИ ПАРА ВЕДУЩАЯ НЕ ТРОГАЕМ ЕЕ
                 minus -= 1

                 print('\n'.join('\t'.join(map(str, row)) for row in matrix))
                 print('\n')
                 continue
             else:

                 save = matrix[i][i]

                 matrix[i][i] = matrix[i][minus]

                 matrix[i][minus] = save

                 minus -= 1#ИНДЕКС ДЛЯ ПОБОЧНОЙ ДИАГОНАЛИ
                 print('\n'.join('\t'.join(map(str, row)) for row in matrix))
                 print('\n')
        matrix = c.deepcopy(matrix_ORIGINAL) #КОГДА ЗАКОНЧИМ С ПАРОЙ ПРИВОДИМ К ИСХОДНОЙ РАБОЧУЮ МАТРИЦУ
        minus = n-1 #ПРИВОДИМ К ИСХОДНОМУ ЗНАЧЕНИЕЮ ИНДЕКС ПОБОЧНОЙ ДИАГОНЛИ
        flag += 1#ПЕРЕМЕННАЯ ДЛЯ УКАЗАНИЯ ВЕДУЩЕЙ ПАРЫ

    """-------------------------------------"""
    """    С ПОМОЩЬЮ БИБЛИОТЕКИ ITERTOOLS   """
    """-------------------------------------"""

    flag=0
    res =0
    print("работа через itertools")

    while flag <= n:
        for i in range(0,n):
            if i == flag:
                print(f'\n{main_line[i]},{second_line[i]}\n ведущая пара')
                res=main_line[i]
                continue
            else:
                result = list(it.permutations((main_line[i],second_line[i]),2))
                if result[0][0] != res:
                    print(f'пара в исходной матрице до  {result[0]} пара после {result[1]}\n')

        flag += 1


"""-------------------------------------------------------------------------------------------"""
"""    ВО ВТОРОЙ ЧАСТИ МЫ ОТБРАСЫВАЕМ КОМБИНАЦИЮ  У КОТОРОЙ ВЕДУЩАЯ ПАРА В СУММЕ БОЛЬШЕ n^2   """
"""-------------------------------------------------------------------------------------------"""
if choose == 1:
    n_on_n = n*n
    while flag < n: #ИДЕМ ДО ТЕХ ПОР ПОКА НЕ ПРОЙДЕМ ПО ВСЕМ ПАРАМ
        print ("введущая пара ", matrix[flag][flag],matrix[flag][minus-flag])
        if matrix[flag][flag] + matrix[flag][minus-flag] < n_on_n:

            for i in range (0,n):

                 if i == flag:#ЕСЛИ ПАРА ВЕДУЩАЯ НЕ ТРОГАЕМ ЕЕ

                         minus -= 1

                         print('\n'.join('\t'.join(map(str, row)) for row in matrix))
                         print('\n')
                         continue

                 else:

                     save = matrix[i][i]

                     matrix[i][i] = matrix[i][minus]

                     matrix[i][minus] = save

                     minus -= 1#ИНДЕКС ДЛЯ ПОБОЧНОЙ ДИАГОНАЛИ
                     print('\n'.join('\t'.join(map(str, row)) for row in matrix))
                     print('\n')

            else:

                None

        matrix = c.deepcopy(matrix_ORIGINAL) #КОГДА ЗАКОНЧИМ С ПАРОЙ ПРИВОДИМ К ИСХОДНОЙ РАБОЧУЮ МАТРИЦУ
        minus = n-1 #ПРИВОДИМ К ИСХОДНОМУ ЗНАЧЕНИЕЮ ИНДЕКС ПОБОЧНОЙ ДИАГОНЛИ
        flag += 1#ПЕРЕМЕННАЯ ДЛЯ УКАЗАНИЯ ВЕДУЩЕЙ ПАРЫ

    """-------------------------------------"""
    """    С ПОМОЩЬЮ БИБЛИОТЕКИ ITERTOOLS   """
    """-------------------------------------"""

    flag = 0
    res = 0
    print("работа через itertools")

    while flag <= n:
        for i in range(0, n):
            if i == flag:
                print(f'\n{main_line[i]},{second_line[i]}\n ведущая пара')

                res = main_line[i]
                sec = second_line[i]
                continue
            else:
                if res + sec >= n_on_n:
                    continue
                result = list(it.permutations((main_line[i], second_line[i]), 2))
                if result[0][0] != res:
                    print(f'пара в исходной матрице до  {result[0]} пара после {result[1]}\n')

        flag += 1
