'''Задача 28: Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
*Пример:*
2 2
>> 4 '''

a = int(input("Введите первое число : "))
b = int(input("Введите второе число : "))

def my_sum(a, b,s):
    if b < 0 and a < 0:
        print(f"результат: {s}")
        return a
    b -= 1
    if b >= 0 :
        s = 1 + s
    a -= 1
    if a >= 0 :
        s = 1 + s
    my_sum(a, b,s)

s = 0
my_sum(a, b,s )

# или такое решение
# def summa(a, b):
# if b == 0:
# return a
# sum = 1+summa(a, b-1)
# return (sum)


# print(summa(int(input("First number = ")), int(input("Second number = "))))