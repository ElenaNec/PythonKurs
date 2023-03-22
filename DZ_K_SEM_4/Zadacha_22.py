"""Задача 22: Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. (может быть с повторениями).

Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах."""

from random import randint

number_1 = [randint(1,8) for _ in range(int(input("Введите количество эл-тов первого множества : ")))]
number_2 = [randint(1,8) for _ in range(int(input("Введите количество эл-тов второго множества : ")))]

print(number_1)
print(number_2)
number_1.sort
number_2.sort

number_1 = set(number_1)
number_2 = set(number_2)
number = number_1.intersection(number_2)

print( number)

