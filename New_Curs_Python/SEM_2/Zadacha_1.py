# Напишите программу, которая получает целое число и возвращает его двоичное,
# восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

a = 2345
result = ""
b = oct(a)
while a > 0:
    result = str(a % 8) + result
    a = a//8
print(b, result)
if result == b[2:]:
    print(True)
