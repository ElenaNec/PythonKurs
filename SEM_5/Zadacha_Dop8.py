"""Найти площадь сложной фигуры. Фигура может состоять из прямоугольника, круга, треугольника"""

from Modul_k_Zadacha_Dop8 import *

def all_square():
    n = int(input("введите количество фигур: "))
    s = 0
    for num_fig in range(n):
        plus_minus = input(" - или +: ")
        symbol = 1
        if plus_minus == "-":
            symbol = -1
        fig = input("введите фигуру(т, п, к): ")
        if fig == "п":
            n = int(input("введите ширину: "))
            m = int(input("введите длину: "))
            s += symbol*rect(m, n)
        elif fig == "т":
            h = int(input("введите высоту: "))
            m = int(input("введите основание: "))
            s += symbol*tri(m, h)
        else:
            r = int(input("ввдите радиус: "))
            s += symbol*circ(r)
    return s

print(all_square())
