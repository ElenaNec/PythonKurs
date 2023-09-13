# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: 
# “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

number = int(input("Введите не отрицательное число меньше 100000 : "))
if  0 <= number < 100000: 
    for i in range (2, number):
        if number % i == 0:
            print(f" Число {number} - составное")
            exit()
    print(f" Число {number} - простое")
    
else:
    print(f" Число {number} должно быть неотрицательное и меньше 100000")