import itertools
from colorama import Fore, Back, Style, init   # importing colorama package to give a contrasting colors to our game.
init()                                         #to use colorama in windows we need to call the  init function.


def win(current_game):                         # win function defined! which contains horizontal, left diagonal, right diagonal, and down functions

    def all_same(l):                           # compares the given element with others.
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal                                # user will be decalred winner if he has all of his 'X' or 'O' in horizontal row
    for row in game:
        print(row)
        if all_same(row):
            print(f'winner{row[0]} is the winner Horizontal (-)' )
            return True

    # Diagonal                                  # user will be decalred winner if he has all of his 'X' or 'O' in Diagnol manner
    diags= []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[col][row])
    if all_same(diags):
        print(f"winner{diags[0]} is the winner Diagonally (/)!" )      #right to left diagonal
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"winner{diags[0]} is the winner Diagonally (\\)!" )      #left to right diagonal
        return True

    # Vertical                              # user will be decalred winner if he has all of his 'X' or 'O' in vertical column
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"winner{check[0]} is the winner Vertically(|)!" )
    return False

def game_board(game_map,player=0, row=0, column=0, just_display= False):    #main function
    try:
        if game_map[row][column] != 0:                                      # exception to handle 0
            print("This position is occupado! Choose another")
            return game_map, False
        print("   "+"  ".join(str(i) for i in range(len(game_map))))
        if not just_display:
            game_map[row][column] = player
        

        for count, row in enumerate(game_map):
         
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)


        return game_map, True

    except IndexError as e:
        print("Error: make sure you input row/column as 0 1 or 2?",e)   # if input is other than 0,1,2
        return game_map , False

    except Exception as e:
        print('something went very wrong',e)
        return game_map , False

play = True
player = [1 , 2]
while play:
    game_size = int(input("what size game of tic tac toe? "))           # game size is given by the user
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    print(game)
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while  not game_won:                                    # untill some person wins
        current_player = next(player_choice)
        print(f"current_player: {current_player}")
        played = False

        while not played:
            column_choice  = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice  = int(input("what row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")       # if users enjoys game and wants to paly it again
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print('Byeeee!!!')
                play = False
            else:
                print("Not a valid answer, so... see you later")
                play = False
