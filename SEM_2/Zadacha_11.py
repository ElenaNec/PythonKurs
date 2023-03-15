# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6 
# fibonachy = {0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711 }


number = int(input(" Введите число, больше 1 : "))
count = 2
number0 = 0
number1 = 1
key = True
while key:
    numberFibonacci = number0 + number1
    if numberFibonacci < number:
        number0 = number1
        number1 = numberFibonacci
        count += 1
    elif numberFibonacci == number:
        count += 1
        key = False
    else:
        count = -1
        key = False
print (f'Число {number} является {count} числом Фибоначчи')
        
        
# или можно так
# number = int(input(" Введите число, больше 1 : "))
# number0 = 0
# result = 1
# i = 1
# while result < number:
#     number0, result = result, number0 + result
#     i += 1
# if result == number:
#    print (f'Число {number} является {i} числом Фибоначчи')
# else:
#     print (f'Число {number} не является числом Фибоначчи')
    