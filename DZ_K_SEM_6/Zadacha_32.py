'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону (
т.е. не меньше заданного минимума и не больше заданного максимума)'''


from random import randint

array = [randint(-10,10) for _ in range(int(input('Введите количество эл-тов массива: ')))]
print(array)

a = int(input('Введите начало диапазона: '))
b = int(input('Введите конец диапазона: '))
#print(f"Диапазон: ({a} , {b})")

new_array =[]
for i in range(len(array)):
    if a < array[i] < b :
        new_array.append(i)
        
print(f"Индексы элементов массива, принадлежащих диапазону ({a} , {b}) :  {new_array}")

# Эталонное решение :
# for i in range(len(array)):
#     if a < array[i] < b:
#         print(i)







