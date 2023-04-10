'''Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных'''

import os


def writing_person():
    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(
    f"фамилия:{lastname}   имя:{name}   отчество:{surname}   телефон:{tel}\n\n")
    data.close()


def search():
    lookfor = input("кого ищем? ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)
                
def my_replace_and_delite():
    # if search():
        print('Если вы хотите изменить данные нажмите - 1, если хотите удалить данные нажмите - 2 ')
        ask = int(input())
        counter = 0
        if ask == 1 :
            temp = input('Что вы хотите заменить? ')
            with open("phonebook.txt", "r+", encoding="utf-8") as data:
                lines = data.readlines()
                for line in lines:
                    if temp in line:
                        temp1 = input(f'На что меняем "{temp}"? \n')
                        line1 = line.replace(temp, temp1, 1)
                        lines[counter] = line1
                        data.close()
                        data = open('phonebook.txt', "w", encoding="utf-8")
                        data.writelines(lines)
                        data.close()
                    counter += 1
        elif ask == 2 :
            temp = input('какие данные вы хотите удалить? ')
            with open("phonebook.txt", "r", encoding="utf-8") as data:
                lines = data.readlines()
                for line in lines:
                    if temp in line:
                        temp1 = "-_-"
                        line1 = line.replace(temp, temp1, 1)
                        lines[counter] = line1
                        data.close()
                        data = open('phonebook.txt', "w", encoding="utf-8")
                        data.writelines(lines)
                        data.close()
                    counter += 1
        else:
            print('Введите корректное действие: 1 или 2 ')
            ask = int(input())
            
            


def print_phonebook():
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def load():
    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")



print("""1 - добавление, 
2 - поиск, 
3 - вывод на экран, 
4 - импорт из файла,
5 - изменить или удалить данные""")
ask = int(input())
if ask == 1 :
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    load()
elif ask == 5:
    my_replace_and_delite()
else:
    print("нет такой команды")