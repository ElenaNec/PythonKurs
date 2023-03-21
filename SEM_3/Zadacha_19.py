'''Задача №19. Общее обсуждение
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3]'''

from random import randint
<<<<<<< HEAD

n = int(input("Введите количество чисел в списке :"))
k = int(input(" Введите число K : "))
list_1 = [randint(1,10) for _ in range(n)]
print(list_1)
j = 0
for i in range(k, n):
    list_1.insert(j, list_1[i])  # на позицию j добавляем эл-т list_1[i]
    list_1.pop(i+1)  # удаление из списка (i+1)го эл-та
    j += 1
print(list_1)
=======
n = int (input("Введите количество элементов "))
K = int (input("Введите число K "))
list_1 = [randint(1, 10) for _ in range(n)]
print(list_1)
j = 0
# for i in range(K, n):
#     list_1.insert(j, list_1[i])
#     list_1.pop(i + 1)
#     j += 1
print(list_1)

# или такое решение:
# numbers = [1, 2, 3, 4, 5]
# k = int(input()) % len(numbers)
# for i in range(k-1):
#     numbers.insert(0, numbers.pop())
# print(numbers)

# или такое решение:

# numbers = [1, 2, 3, 4, 5]
# k = int(input())
# k = k%len(numbers)
# print(numbers[k:]+numbers[:k])
>>>>>>> 5b0ec50b6ec1a795c33da907c296c44842234784
