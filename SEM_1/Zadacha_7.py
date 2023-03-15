# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

god = int(input("Введите год : "))

if ((god % 4 == 0) and (god % 100 != 0) or (god % 400 == 0)):
    print(f"{god} - является високосным")
else:
   print(f"{god} - не является високосным") 