# Создайте несколько переменных заканчивающихся и
# не оканчивающихся на “s”.
# Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def change():
    a = globals()
    for key, value in a.items():
        if key[-1] == "s":
            a[key[:-1]] = value
            a[key] = None


cat = "1"
cats = "2"
dog = "3"
dogs = "4"

change()
print(globals())
