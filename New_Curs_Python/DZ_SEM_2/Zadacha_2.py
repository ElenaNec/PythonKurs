# Напишите программу, которая принимает две строки
# вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions

a = int(input("Введите числитель первой дроби : "))
b = int(input("Введите знаменатель первой дроби : "))
c = int(input("Введите числитель первой дроби : "))
d = int(input("Введите знаменатель первой дроби : "))

operation = int(
    input("Введите цифру 1, если хотите сложить дроби и 2 - перемножить дроби : "))
if operation == 1:
    if b == d:
        result = a + c
        print(f"{a}/{b} + {c}/{d} = {result}/{b}")
    else:
        result = (a*d) + (c*b)
        print(f"{a}/{b} + {c}/{d} = {result}/{d*b}")
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(c, d)
    print(f1 + f2)
elif operation == 2:
    print(f"{a}/{b} * {c}/{d} = {a*c}/{d*b}")
    f1 = fractions.Fraction(a, b)
    f2 = fractions.Fraction(c, d)
    print(f1 * f2)

else:
    print(f"Операция {operation} не определена")
