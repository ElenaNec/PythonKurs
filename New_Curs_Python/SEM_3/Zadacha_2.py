# Пользователь вводит данные.
# Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

n = "-56.9"
if n.isdigit():
    print(int(n))
if "." in n:
    if "-" in n:
        n = n.replace(__old: '-', __new: '')
        flag = True
    left, right = n.split(".")
    if left.isdigit() and right.isdigit():
        if flag:
            print(-float(n))
        else:
            print(float(n))
if n != n.lower():
    print(n.lover())
else:
    print(n.upper())
