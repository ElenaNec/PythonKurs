'''Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.'''




a = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность элементов: "))
n = int(input("Введите количество элементов: "))

# Через цикл for:
array = []
temp = 0
for _ in range(1,n+1):
    array.append(a + temp) 
    temp = temp + d
print(array, end=" ")

# Эталонное решение :
# for i in range(n):
#     print(a1 + i * d)

# Через рекурсию :
# print(a, end=" ")
# def fill_array(a, d, n):
#     if n == 1:
#         return a
#     print(a + d, end=" ")
#     fill_array(a + d, d, n-1)
    
# fill_array(a, d, n)


# Через цикл while:
# array = []
# a = a + (n-1)* d
# array.append(a) 
# temp = 0
# while n > 1:
#     temp += d
#     array.insert(0, a - temp) 
#     n = n -1
# print(array, end=" ")