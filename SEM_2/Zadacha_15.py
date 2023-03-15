'''Задача №15. 
Иван Васильевич пришел на рынок и решил
купить два арбуза: один для себя, а другой для тещи.
Понятно, что для себя нужно выбрать арбуз
потяжелей, а для тещи полегче. Но вот незадача:
арбузов слишком много и он не знает как же выбрать
самый легкий и самый тяжелый арбуз? Помогите ему!

Пользователь вводит одно число N – количество
арбузов. Вторая строка содержит N чисел,
записанных на новой строчке каждое. Здесь каждое
число – это масса соответствующего арбуза.
т.е. Вывести максимальное и минимальное
Input: 5 -> 5 1 6 5 9
Output: 1 9 '''

from random import randint
n = int(input('Введите количество арбузов для выбора : '))
minimum = 100
maximum = 0
i = 0
while i < n:
    watermelon = randint(1,20)
    print(watermelon)
    if watermelon < minimum:
        minimum = watermelon
        
    elif watermelon > maximum:
        maximum = watermelon
    i += 1
print()
print(f'min вес = {minimum} , max вес = {maximum}')
print()


# другое решение
'''
from random import randint

watermelon = int(input("введите количество арбузов: "))
max = randint(1, 50)
print(max)
min = max
for i in range(watermelon-1):
    x = randint(1, 50)
    print(x)
    if max < x:
        max = x
    elif min > x:
        min = x
print(f"самый тяжелый арбуз весит {max} кг, а самый легкий {min} кг")  
''' 