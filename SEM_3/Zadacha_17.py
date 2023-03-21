'''Задача 17.
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6'''

from random import randint

n = int(input("Введите количество чисел в списке :"))
list_1 = [randint(1,10) for _ in range(n)]  # если в цикле не используется цикличная переменная то пишется нижнее подчеркивание

# строчку выше можно было записать так:
# list_1 = []
# for i in range(n):
#     list_1.append(randint(1,10)) # создается рандомный список

print(list_1)
print(len(set(list_1)))  # список list_1 переводится во множество и выводится кол-во эл-тов множества
