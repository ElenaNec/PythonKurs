'''Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод: Вывод:
1 2 3 2 3 2'''

list_num = input('Введите список чисел: ').split()
counter = 0
for i in range(len(list_num) - 1):
    num = list_num[i + 1:].count(list_num[i])
    counter += num
print(f'Количество пар элементов: {counter}')