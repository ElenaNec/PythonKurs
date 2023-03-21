'''Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов 
в массиве. В последующих  строках записаны N целых чисел Ai. 
Последняя строка содержит число X

*Пример:*

    5
    1 2 3 4 5
    6
    -> 5'''

n = int(input("ВВедите число элементов массива = "))
x = int(input("ВВедите число X = "))
list = [int(input(f"Введите {i} элемент массива ")) for i in range(n)]
print(list)
uniq = set()
elem_min_diff = list[0]
min_diff = abs(list[0]-x)
for num in list[1:]:
    cur_diff = abs(num-x)
    if cur_diff < min_diff and num != x:
        elem_min_diff = num
        min_diff = cur_diff
        uniq.clear()
        uniq.add(elem_min_diff)
    elif cur_diff == min_diff and num != x:
        uniq.add(num)

print(f"Самые близкие числa к {x} :")
print(*uniq)
