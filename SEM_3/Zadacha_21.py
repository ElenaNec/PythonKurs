'''Напишите программу для печати всех уникальных значений в словаре.

Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


Примечание: Список словарей задан изначально. Пользователь его не вводит'''

my_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "},
{" VIII":" S007 "}] # заданный список словарей
print(my_list)
n = set() # создается пустое множество
for dict_i in my_list: # этот цикл перебирает словари внутри списка
    print(dict_i) 
    for key in dict_i:  # этот цикл перебирает ключи в словарях
        print(dict_i[key].strip()) # strip() убирает лишние пробелы в строковых переменных
        n.add(dict_i[key])
print(n)
     
# или такое решение:
# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII": "S007"}]
# n = set() # создается пустое множество
# for dict_i in dictionary: # проходим по эл-там списка (т.е по словарям)
# #print(i)
#     for key in dict_i:
#         #print(i[j])
#         n.add(dict_i[key]) # обращаемся к зн-ям словарей по ключам и добавляем зн-я в пустое мн-во
# print(n)

# или такое решение:
# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# unique_values = [] # создается список куда будем записывать уникальные эл-ты
# for item in data: # в списке перебираем эл-ты (т.е словари)
#     for value in item.values(): # из словаря получаем значение с помощью метода values()
#         value = value.strip() # метод .strip удаляеn лишние пробелы вокруг значений
#         if value not in unique_values: # проверяем получинные зн-я на уникальность
#             unique_values.append(value)
# print(set(unique_values))
