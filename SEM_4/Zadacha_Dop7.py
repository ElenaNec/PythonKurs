""" Крестики нолики """

import os
def print_field(field):
    print(field[0],field[1],field[2])
    print(field[3],field[4],field[5])
    print(field[6],field[7],field[8])

def check(symbol):
    player = input(f"куда ставить {symbol}: ")
    while player not in my_field or player in "OX" :
        print("не корректный ввод, попробуйте еще раз")
        player = input(f"куда ставить {symbol}: ")
    return player

def win(field):
    if (field[0]== field[1] == field[2]
    or field[3]== field[4] == field[5]
    or field[6]== field[7] == field[8]
    or field[0]== field[3] == field[6]
    or field[1]== field[4] == field[7]
    or field[2]== field[5] == field[8]
    or field[0]== field[4] == field[8]
    or field[2]== field[4] == field[6]):
        return True
    return False

my_field = ["1","2","3","4","5","6","7","8","9"]

for step in range(1,10):
    os.system("cls")
    print(f"\n{step} ход")
    print_field(my_field)
    cur_symbol = "X" if step % 2 else "O"
    first_player = check(cur_symbol)
    my_field[int(first_player)-1] = cur_symbol
    if win(my_field):
        print_field(my_field)
        print(f"{cur_symbol} выиграл")
        break