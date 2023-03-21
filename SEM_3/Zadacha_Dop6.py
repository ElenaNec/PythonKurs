'''Сделать матрицу с помощью вложенного генератора списков'''

from random import randint
my_list = [[col * row for col in range(9)] for row in range(1, 6)] # row - строка, col -столбец

print(my_list)

# В генераторе списков можно использовать конструкцию if- else
new_list = [elem for elem in range(9) if not elem % 2]
print(new_list)
new_list = [elem if elem % 2 else 0 for elem in range(9)]

new_list = [elem if elem % 2 else 
('да' if elem % 3 == 0 else 0)
for elem in range(9)]