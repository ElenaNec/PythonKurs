'''Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]

Output: 6
'''

from random import randint

list_1 = []
#list_2 = set()
n = int (input("Введите количество элементов "))
for i in range(n):
    list_1.append(randint(1, 10))
    print(list_1)
print(len(set(list_1)))
