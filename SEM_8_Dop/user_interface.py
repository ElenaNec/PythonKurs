from logger import *

def interface():
    print("1 - записать данные, 2 - вывести данные")
    var = input('введите номер варианта: ')
    while var not in ('1','2'):
            print('вариант не верный')
            var =  input('введите номер варианта: ')
            
    if var == 1:
        input_data()
    else:
        print_data()