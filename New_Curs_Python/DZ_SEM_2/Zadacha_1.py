# Напишите программу,
# которая получает целое число
# # и возвращает его шестнадцатеричное строковое представление.
# # Функцию hex используйте для проверки своего результата.
# 10, 11, 12, 13, 14, 15 записываются буквами A, B, C, D, E, F

number = int(input("Введите целое число : "))
result = ""
comparison = hex(number)
while number > 0:
    remainder = number % 16
    if remainder == 10:
        remainder = "a"
    elif remainder == 11:
        remainder = "b"
    elif remainder == 12:
        remainder = "c"
    elif remainder == 13:
        remainder = "d"
    elif remainder == 14:
        remainder = "e"
    elif remainder == 15:
        remainder = "f"
    result = str(remainder) + result
    number = number//16
print(comparison, result)
if result == comparison[2:]:
    print(True)
