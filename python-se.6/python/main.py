import pyfiglet
import functions

from functions import check_for_equal, select_solo_or_multy, solo_or_multy
from colorama import Fore

score_player_one = 0
score_player_two = 0

text = pyfiglet.figlet_format('tik tok toe', font="slant")
print(text)

game_board = [["-","-","-"],["-","-","-"],["-","-","-"]]


functions.start_timer()

functions.show_board(game_board)

functions.HR()

user_selection = int(input("1 for play solo , 2 for play multy "))

while 1:

    #start game for player  1:

    row = functions.take_row(1) # player 1 turn
    col = functions.take_col(1)

    functions.is_cell_empty(game_board, row ,col,f"{Fore.RED}x{Fore.WHITE}",1)
    functions.show_board(game_board)

    functions.HR()

    functions.check_player_one_win(game_board,score_player_one,score_player_two)
    check_for_equal(game_board)

    # start game for player  2:

    # functions.check_for_opponent(opponent_status,game_board,score_player_one,score_player_two)

    solo_or_multy(user_selection,game_board,score_player_one,score_player_two)







