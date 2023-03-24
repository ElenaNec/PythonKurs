"""Модуль с функциями для подсчета площадей фигур"""

def rect(n,m):
    s= n*m
    return s

def tri(h,m):
    s = 0.5*h*m
    return s

def circ(r):
    return 3.14*r**2

def main():   # эта функция для вызова главной программы
    print(rect(2,3))
    print(tri(2,3))
    print(circ(2))

if __name__ == "__main__":   # условие при котором функция main вызывается только из этой программы
    main()                      # при вызове модуля "my_modul"из другой программы, ф-я main не будет отрабатывать