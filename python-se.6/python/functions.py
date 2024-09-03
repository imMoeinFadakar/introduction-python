from operator import index
from readline import set_history_length

from numpy.f2py.symbolic import as_ne
from orca.settings import brailleFlashTime

import random
import time
from colorama import Fore

score_X = 0
score_O = 0




def add_player_one_score(num):
    num += 1
    return num


def add_player_two_score():
    global score_O

    score_O += score_O + 1

    return score_O

def board_clean(board):
        for submenu in board:
            submenu.clear()
            submenu.append("-")
            submenu.append("-")
            submenu.append("-")


def show_board(game_board):
    for row in game_board:
        for cell in row:
            print(cell, end=' ')
        print()

def take_row(player_number):
    print(f"its player {player_number} turn")
    while 1:
        num = int(input(f"Enter row player:{player_number} :")) - 1
        if num > 2:
            print("to height!")

        elif num < 0:
            print("to low !")

        else:
            return num


def take_col(player_number):
    print(f"its player {player_number} turn")
    while 1:
        num = int(input(f"Enter col player:{player_number} :")) - 1
        if num > 2:
            print("to height!")

        elif num < 0:
            print("to low !")

        else:
            return num




def HR():
    print("________________________________")


def is_cell_empty(board,row,col,xo,player):
     while 1:
        if board[row][col] == "-":
            fill_empty_cell(board,row,col,xo)
            return print("I added your mark :))")
        else:
            print("this position is not empty!")
            row = take_row(player)
            col = take_col(player)

def fill_empty_cell(board,row,col,xo):
     board[row][col] = xo
     return print("your mistake is fixed now!")

def check_player_one_win(border,scoreX,scoreO):

    for row in border:
        if all(element == f"{Fore.RED}x{Fore.WHITE}" for element in row):
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][0] == f"{Fore.RED}x{Fore.WHITE}" and border[1][1] == f"{Fore.RED}x{Fore.WHITE}" and border[2][2] == f"{Fore.RED}x{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)


        elif border[0][2] == f"{Fore.RED}x{Fore.WHITE}" and border[1][1] == f"{Fore.RED}x{Fore.WHITE}"and border[2][0] == f"{Fore.RED}x{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][0] == f"{Fore.RED}x{Fore.WHITE}" and border[1][0] == f"{Fore.RED}x{Fore.WHITE}"and border[2][0] == f"{Fore.RED}x{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][1] == f"{Fore.RED}x{Fore.WHITE}" and border[1][1] == f"{Fore.RED}x{Fore.WHITE}"and border[2][1] == f"{Fore.RED}x{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][2] == f"{Fore.RED}x{Fore.WHITE}" and border[1][2] == f"{Fore.RED}x{Fore.WHITE}"and border[2][2] == f"{Fore.RED}x{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)


def check_player_two_win(border,scoreX,scoreO):
    for row in border:
        if all(element == f"{Fore.BLUE}o{Fore.WHITE}" for element in row):
            print(f"player two WON! ")
            return ask_for_continue(border)

        elif border[0][0] == f"{Fore.BLUE}o{Fore.WHITE}" and border[1][1] == f"{Fore.BLUE}o{Fore.WHITE}" and border[2][2] == f"{Fore.BLUE}o{Fore.WHITE}":
            print(f"player two WON! ")
            return ask_for_continue(border)

        elif border[0][2] == f"{Fore.BLUE}o{Fore.WHITE}" and border[1][1] == f"{Fore.BLUE}o{Fore.WHITE}" and border[2][0] == f"{Fore.BLUE}o{Fore.WHITE}":
            print(f"player two WON! ")
            return ask_for_continue(border)

        elif border[0][0] == f"{Fore.BLUE}o{Fore.WHITE}" and border[1][0] == f"{Fore.BLUE}o{Fore.WHITE}" and border[2][
            0] == f"{Fore.BLUE}o{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][1] == f"{Fore.BLUE}o{Fore.WHITE}" and border[1][1] == f"{Fore.BLUE}o{Fore.WHITE}" and border[2][
            1] == f"{Fore.BLUE}o{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)

        elif border[0][2] == f"{Fore.BLUE}o{Fore.WHITE}" and border[1][2] == f"{Fore.BLUE}o{Fore.WHITE}" and border[2][
            2] == f"{Fore.BLUE}o{Fore.WHITE}":
            print(f"player one WON! ")
            return ask_for_continue(border)



def ask_for_continue(boarder):
    answer = int(input(" 1 = 'continue' or 0 = 'exit'"))
    if answer == 1:
        board_clean(boarder)
        return print("yhoooo! lets continue baby!")
    elif answer == 0:
        stop_timer()
        return exit("good lock ")


def check_for_equal(border):
    filled_cells = 0
    for row in border:
         for item in row:
            if item != "-":
                filled_cells += 1
                if filled_cells == 9:
                    print("Draw !")
                    board_clean(border)



def select_solo_or_multy(choice,border):
    if choice == 1:
         print("you selected solo play!")
         return 1

    elif choice == 2:
         print("you selected multy play!")
         return 2


def add_bot(border):
    while 1:
        random_number_row = random.randint(0,2)
        random_number_col = random.randint(0,2)
        if border[random_number_row][random_number_col] == "-":
            border[random_number_row][random_number_col] = f"{Fore.BLUE}o{Fore.WHITE}"
            break


def play_with_bot(board,scoreX,scoreO):

        add_bot(board)
        show_board(board)
        check_player_two_win(board, scoreX, scoreO)
        HR()
        check_for_equal(board)


def multy_player(board,scoreX,scoreO):

    row = take_row(2)
    col = take_col(2)

    is_cell_empty(board, row, col, f"{Fore.BLUE}o{Fore.WHITE}", 2)
    show_board(board)
    check_player_two_win(board, scoreX, scoreO)
    HR()
    check_for_equal(board)


def solo_or_multy(user_selection,bored,score_player_one,score_player_two):

    if user_selection == 1:

        return play_with_bot(bored,score_player_one,score_player_two)

    elif user_selection == 2:

        return multy_player(bored,score_player_one,score_player_two)

def start_timer():
    global start_time
    start_time = time.time()


def stop_timer():
    global start_time
    elapsed_time = time.time() - start_time
    print(f"\nTimer stopped. Total time: {elapsed_time:.2f} seconds")



