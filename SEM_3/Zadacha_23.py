'''Задача №23. Решение в группах
Дан массив, состоящий из целых чисел. Напишите
программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента
с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
Примечание: Пользователь может вводить значения
списка или список задан изначально.'''

from random import randint
n = int (input("Введите количество элементов "))
counter = 0
list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
for i in range(1, n):
    if list_1[i-1] < list_1[i]:
        counter += 1
print(counter)

# или такое решение :
# massiv = input("Введите список чисел через пробел: ").split()
# massiv = [int(num) for num in massiv] # преобразуем каждый элемент списка из строкового в целочисленный тип

# quantity = 0
# for i in range(1, len(massiv)):
#     if massiv[i] > massiv[i-1]:
#         quantity += 1
# print(quantity)
