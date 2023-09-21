# Создайте словарь со списком вещей для похода в качестве ключа 
# и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. 
# Достаточно вернуть один допустимый вариант.

list_of_things = {"палатка": 2, "спальник": 1, "топор": 2, "еда": 2, "вода": 1, "вещи": 3}

backpack_weight = int(input("Укажите максимальную вместимость веса рюкзака : "))

weight_things = list(list_of_things.values())
name_things = list(list_of_things.keys())
print(name_things)

weight = 0
for el in range(len(weight_things)):
    weight += weight_things[el]
print(weight)

print("В рюкзак поместится : ")
if backpack_weight >= weight:
    for keys in name_things:
        print(keys)
else:
    weight_difference = weight - backpack_weight
    a = 0
    for el in weight_things:
        if el == weight_difference:
            # del list_of_things[name_things[a]]
            # new = list(list_of_things.keys())
            name_things.remove(name_things[a])
            break
        a += 1
    print('\n'.join(name_things))
        

