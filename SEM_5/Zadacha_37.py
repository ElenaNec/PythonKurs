"""Дано натуральное число N и последовательность из N элементов. 
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

Input: 2 -> 3 4
Output: 4 3"""

def f(n):
    if n == 0:
        return
    k = int(input())
    f(n-1)
    print(k, end=' ')

n = int(input("Введите число : "))
f(n)

# def f(n):
#     if n == 0:
#         return ''
#     k = int(input())
#     return f(n-1) + f' {k}'

# n = int(input("Введите число : "))
# print(f(n)[1:])  # [1:] написали чтобы не было при выводе пробела в начале строки делаем вывод со 2го символа
    

# def new_max(n, str):
#     if n == 0:
#         print(str)
#         str = str[::-1]
#         print(str)
#         return
#     str += input("Введите эл-т : ") + " "
#     return new_max(n-1, str)

# n = int(input("Введите число : "))
# new_max(n, "")