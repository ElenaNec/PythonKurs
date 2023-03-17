'''Задача 12: 
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
2) Пользователь вводит два числа построчно, первое – сумма двух чисел, второе – произведение этих чисел. 
Нужно вывести исходные числа.'''

from math import sqrt


print("Загадайте два числа!")

sum = int(input("Напишите чему равна сумма загаданных чисел : "))
proizvedenie = int(input("Напишите чему равно произведение загаданных чисел : "))

# print(f"Загаданные числа a = { (sum - sqrt(((-sum)**2)-4*proizvedenie))/2} , b = { (sum + sqrt(((-sum)**2)-4*proizvedenie))/2}")

for x in range(1,sum//2+2):
    y = sum-x
    if x*y == proizvedenie:
        print (f"Искомые числа {x} и {y}")