'''Задача 14: Требуется вывести все целые степени двойки 
(т.е. числа вида 2k), не превосходящие числа N.
Пример: 10 -> 1 2 4 8'''

number = int(input("Введите число : "))
i = 0
while i < number:
    stepen = 2 ** i
    i += 1
    if stepen <= number:
        print(stepen, end = " ")
    else:
        break