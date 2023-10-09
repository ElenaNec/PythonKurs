# Создайте функцию-генератор. 
# Функция генерирует N простых чисел, начиная с числа 2. 
# Для проверки числа на простоту используйте правило: 
# “число является простым, если делится нацело только на единицу и на себя”.


import typing

def simpl_n(num : int) -> bool:
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def gen_simpl(n : int) -> typing.Generator:
    for i in range(2, 100):
        if simpl_n(i):
            yield i
            
            
for i in gen_simpl(100):
    print(i)
    
#  строку 21-22 можно записать так
# result = gen_simpl(100)
# ''' выведет 5 простых чисел'''
# for i in range(5):
#     print(next(result)) 
