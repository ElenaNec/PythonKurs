'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 '''

a = int(input("Введите число : "))
b = int(input("Введите степень в которую надо возвести число : "))

def kvadrat_num(a, b, temp):
    if b == 1:
        print(f"результат: {a}")
        return a
    b -= 1
    kvadrat_num(a*temp, b, temp)

temp = a
kvadrat_num(a, b, temp)