'''Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
в каком они идут в первом массиве), которых нет во втором массиве. 
Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. Затем элементы второго массива
Ввод: Вывод:
7 3 3 2 12
3 1 3 4 2 4 12
6
4 15 43 1 15 1 (каждое число вводится с новой строки)'''

from random import randint

def FillArray (arraySize):
    array = []
    for i in range (arraySize):
        num = randint(1,10)
        array.append(num)
    return array

def FindUniqueNumbers (array1, array2):
    for i in range (len_array1):
        if array1[i] not in array2:
            print (array1[i],end=" ")

len_array1 = int(input("Введите количество элементов первого массива "))
my_array1 = FillArray (len_array1)

len_array2 = int(input("Введите количество элементов второго массива "))
my_array2 = FillArray (len_array2)

FindUniqueNumbers (my_array1, my_array2)