#!/usr/bin/python

import re
from IPython.display import clear_output
import itertools

p1_marker = ''
p1_type = ''
p2_marker = ''
p2_type = ''
memorize = False
game = True

status = '\n'

def new_game():

    global p1_marker
    global p1_type
    global p2_marker
    global p2_type
    global memorize
    global board

    p1_marker = ''

    while p1_marker not in ('x', 'o'):
        p1_marker = input('Player 1: choose x or o: ').lower()

    if p1_marker == 'x':
        p2_marker = 'o'
    else:
        p2_marker = 'x'

    while p1_type not in ('h', 'c'):
        p1_type = input('Player 1: (h)uman or (c)omputer: ').lower()

    while p2_type not in ('h', 'c'):
        p2_type = input('Player 2: (h)uman or (c)omputer: ').lower()

    p1_type = p1_type.replace('c', 'computer').replace('h', 'human')
    p2_type = p2_type.replace('c', 'computer').replace('h', 'human')

    while not memorize:
        tmp = input("Remember these settings for future games (y/n)? ").lower()
        if tmp == 'y':
            memorize = True
        if tmp == 'n':
            break


def replay():

    global board
    repl = None

    while repl not in ('y', 'n'):
        repl = input('Another game (y/n)? ').lower()
        if repl == 'y':
            del board
            new_game()
        else:
            exit()


def new_board():
    
    row1 = []
    row2 = []
    row3 = []
    l_board = [row1, row2, row3]
    
    for f in l_board:
        for g in range(0, 3):
            f.append(' ')
    return l_board


def print_board(brd):

    #print('\n'*100)

    print("Player 1 (%s): %s" %(p1_type, p1_marker))
    print("Player 2 (%s): %s" %(p2_type, p2_marker))
    print("\n   A B C")
    print(f"1 |{brd[0][0]}|{brd[0][1]}|{brd[0][2]}|")
    print(f"2 |{brd[1][0]}|{brd[1][1]}|{brd[1][2]}|")
    print(f"3 |{brd[2][0]}|{brd[2][1]}|{brd[2][2]}|")
    print(status)


def user_move(brd):
    out_list = []
    flag = False
    global game
    global memorize
    global board

    while not flag:
        user_input = input("Enter your move (ex: a1, c2 or use numeric kbrd)\nn for new game, nn for new game with new settings or x for exit: ")
        user_input = user_input.lower()

        if user_input == "x":
            game = False
            flag = True
            exit()

        if user_input == "n":
            flag = True
            del board

        if user_input == "nn":
            memorize = False
            flag = True
            del board
            new_game()

        if user_input == '7':
            return [0, 0]
        if user_input == '8':
            return [1, 0]
        if user_input == '9':
            return [2, 0]
        if user_input == '4':
            return [0, 1]
        if user_input == '5':
            return [1, 1]
        if user_input == '6':
            return [2, 1]
        if user_input == '1':
            return [0, 2]
        if user_input == '2':
            return [1, 2]
        if user_input == '3':
            return [2, 2]

        if len(user_input) == 2:
            if True in (a == b for a in "abc" for b in user_input.lower()) and True in (a == b for a in "123" for b in user_input):
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
                print_board(brd)
                return out_list

            else:
                update_status("BAD INPUT FORMAT", True)
                print_board(brd)

        else:
            update_status("BAD INPUT FORMAT (bad length)", True)
            print_board(brd)


def set_field(brd, position, xo):
    if brd[position[1]][position[0]] == ' ':
        brd[position[1]][position[0]] = xo
        update_status(('Last move: %s, %s' % (position, xo)), True)
        return brd
    else:
        update_status("Field already occupied! Try again.", True)


def check_win(brd):

    # ROW CHECK
    for f in range(0, 3):
        if brd[f][0] == brd[f][1] == brd[f][2] != ' ':
            return brd[f][0]

    # COLUMN CHECK
    for f in range(0, 3):
        if brd[0][f] == brd[1][f] == brd[2][f] != ' ':
            return brd[0][f]

    #MAIN DIAGONAL
    if brd[0][0] == brd[1][1] == brd[2][2] != ' ':
        return brd[0][0]

    #COUNTERDIAGONAL
    if brd[0][2] == brd[1][1] == brd[2][0] != ' ':
        return brd[0][2]

    if list(itertools.chain.from_iterable(brd)).count(' ') == 0:
        return 'draw'

    return False


def next_move_player(brd):

    global p1_marker
    x = list(itertools.chain.from_iterable(brd)).count('x')
    o = list(itertools.chain.from_iterable(brd)).count('o')

    if x == o and p1_marker == 'x' or x < o:
        ret = 'x'
    else:
        ret = 'o'

    if ret == p1_marker:
        pn = 1
    else:
        pn = 2

    print('Player\'s %s (%s) turn...' %(pn, ret))

    return ret

def update_status(msg, override):
    global status
    if override:
        status = "\n"
    status += msg + "\n"


def ai_move(brd):
    return brd

    '''GAME LOGIC'''


while game:



    try:
        board
    except NameError:
        board = new_board()
        if not memorize:
            new_game()
        update_status(("Settings memorized: %s" % memorize), True)


    current_move = user_move(board)
    player = next_move_player(board)

    if current_move:

        print_board(board)

        set_field(board, current_move, player)
        print_board(board)

        winner = check_win(board)

        if winner == 'draw':
            print("As expected, we've got a draw :)")
            replay()

        if winner in ('x', 'o'):
            print("Game over! Winner is %s!" % winner)
            replay()
