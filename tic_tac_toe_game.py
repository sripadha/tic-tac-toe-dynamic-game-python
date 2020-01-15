import itertools
from colorama import Fore, Back, Style, init
init()


def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False
    # Horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f'winner{row[0]} is the winner Horizontal (-)' )
            return True

    # Diagonal
    diags= []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[col][row])
    if all_same(diags):
        print(f"winner{diags[0]} is the winner Diagonally (/)!" )
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"winner{diags[0]} is the winner Diagonally (\\)!" )
        return True

    # Vertical
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            print(f"winner{check[0]} is the winner Vertically(|)!" )
    return False

def game_board(game_map,player=0, row=0, column=0, just_display= False):
    try:
        if game_map[row][column] != 0:
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
        print("Error: make sure you input row/column as 0 1 or 2?",e)
        return game_map , False

    except Exception as e:
        print('something went very wrong',e)
        return game_map , False

play = True
player = [1 , 2]
while play:
    game_size = int(input("what size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]
    print(game)
    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while  not game_won:
        current_player = next(player_choice)
        print(f"current_player: {current_player}")
        played = False

        while not played:
            column_choice  = int(input("what column do you want to play? (0, 1, 2): "))
            row_choice  = int(input("what row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("The game is over, would you like to play again? (y/n)")
            if again.lower() == "y":
                print("restarting")
            elif again.lower() == "n":
                print('Byeeee!!!')
                play = False
            else:
                print("Not a valid answer, so... see you later")
                play = False
