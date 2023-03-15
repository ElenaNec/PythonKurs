'''Напишите программу, которая на вход принимает 5 чисел 
и находит максимальное из них.

Примеры:
- 1, 4, 8, 7, 5 -> 8
- 78, 55, 36, 90, 2 -> 90'''

from random import randint
max=0
for i in range(5):
    x = randint(0,100)
    print(x)
    if x > max:
        max = x
print("\n", max, sep = "")