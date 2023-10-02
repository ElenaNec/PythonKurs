# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode
# каждого символа введённой строки отсортированный по убыванию.

def text_ord(n: str) -> list[int]:
    d = []
    for el in n:
        d.append(ord(el))
    return sorted(list(set(d)), reverse=True)
    ''' Или можно так'''
    # d = set()
    # for el in n:
    #     d.add(ord(el))
    # return sorted(list(d), revers=True)


''' Другая реализация кода'''
# def text_ord(n: str) -> list[int]:
#     return sorted(list(set(map(ord, list(n)))), reverse=True)


n = input()
print(text_ord(n))
