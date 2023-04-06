from data_create import *

def input_data():
    name = name_data()
    lastname = lastname_data()
    phonenum = phone_data()
    adres = adress_data()
    var = input(f""" в каком формате записать данные?
                1 вариант:
                {lastname},
                {name},
                {phonenum},
                {adres}
                2 вариант:
                {lastname}, {name}, {phonenum}, {adres}
                введите номер варианта: """)
    while var not in ('1','2'):
        print('вариант не верный')
        var =  input('введите номер варианта: ')
        
    if var == 1:
        with open("data_first.txt", "a", encoding='utf-8') as file:
            file.write(f"{name}\n{lastname}\n{phonenum}\n{adres}\n\n")
    else:
        with open("data_first.txt", "a", encoding='utf-8') as file:
            file.write(f"{name}; {lastname}; {phonenum}; {adres}\n\n")
        
def print_data(): 
    with open("data_first.txt", "r", encoding="utf-8") as data:
        data_first = data.read()
        # или так
        # data_first = data.readlines()
        # temp = []
        # j = 0
        # for i in range(len(data_first)):
        #     if data_first[i] =="\n" or i == len(data_first)-1:
        #         temp.append("".join(data_first[j : i+1]))
        #         j = i
        # data_first = temp
        #print(*data_first)
        print(data_first)
        
    return data_first

# input_data()
# print_data()