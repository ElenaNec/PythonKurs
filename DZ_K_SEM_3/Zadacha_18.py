'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов 
в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

    5
    1 2 3 4 5
    6
    -> 5'''
    
from random import randint

n = int(input("Введите количество эл-тов в массиве : "))
my_list = []
for elem in range(n):
    my_list.append(randint(1, 20))
print(my_list)
my_list.sort()
print(my_list)

x = int(input("Задайте число : "))
max_bliz = 0
for elem in range(n):
    if x > my_list[n-1]:
        max_bliz = my_list[n-1]
        break
    if my_list[elem] == x :
        max_bliz = my_list[elem]
        break
    else:
        if my_list[elem-1] < x < my_list[elem]:
            if abs(x - my_list[elem-1]) <=  abs(x - my_list[elem]):
                max_bliz = my_list[elem-1]
            else:
                max_bliz = my_list[elem]
        
print(f"К числу {x} самым близким является число {max_bliz} ") 
        
            