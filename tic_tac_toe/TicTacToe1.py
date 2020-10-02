#!/usr/bin/python

import re
from functools import reduce
from IPython.display import clear_output

def set_board():
    
    row1 = []
    row2 = []
    row3 = []
    l_board = [row1, row2, row3]
    
    for f in l_board:
        for g in range(0, 3):
            f.append(' ')
    return l_board

def print_board():

    clear_output()
    print(board)

    print("\n  Player: o\nComputer: x\n")
    print("   A B C")
    print(f"1 |{board[0][0]}|{board[0][1]}|{board[0][2]}|")
    print(f"2 |{board[1][0]}|{board[1][1]}|{board[1][2]}|")
    print(f"3 |{board[2][0]}|{board[2][1]}|{board[2][2]}|\n")

def user_move():
    out_list = []
    flag = False
    while not flag:
        user_input = input("Enter your move (ex: a1, c2 or 3b) or x for exit: ")
        user_input.lower()

        if user_input == "x":
           return None

        if len(user_input) == 2:
            if True in (a == b for a in "abc" for b in user_input.lower()) and True in (a == b for a in "123" for b in user_input):
                flag = True
                if 'a' in user_input:
                    out_list.append(0)
                    user_input = user_input.replace('a','')
                elif 'b' in user_input:
                    out_list.append(1)
                    user_input = user_input.replace('b', '')
                elif 'c' in user_input:
                    out_list.append(2)
                    user_input = user_input.replace('c', '')

                out_list.append(int(user_input)-1)
                print(out_list)
                return out_list

            else:
                print("BAD INPUT - wrong format!")
        else:
            print("BAD INPUT - wrong length!")


def set_field(position, xo):
    board[position[1]][position[0]] = xo
    print_board()


board = set_board()
print_board()

while True:
    set_field(user_move(), 'o')