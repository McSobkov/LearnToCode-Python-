
def update_board(position, player):
    global game_board
    if 0 > position or 9 < position:
        print("Invalid tile")
        return 1
    if game_board[position] == 'X' or game_board[position] == 'Y':
        print("Tile is owned")
        return 1
    else:
        game_board[position] = player
        return 0


def check_winner(board, player):
    if board[0] == board[1] == board[2] or board[3] == board[4] == board[5] or board[6] == board[7] == board[8]:
        print("Player {} wins horizontally!".format(player))
        print_board(board)
        return player
    elif board[0] == board[3] == board[6] or board[1] == board[4] == board[7] or board[2] == board[5] == board[8]:
        print("Player {} wins vertically!".format(player))
        print_board(board)
        return player
    elif board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        print("Player {} wins diagonally!".format(player))
        print_board(board)
        return player
    else:
        return 0


def print_board(board):
    print("----------------------------------")
    print("|          |          |          |")
    print("|          |          |          |")
    print("|     {}    |     {}    |     {}    |".format(board[6], board[7], board[8]))
    print("|          |          |          |")
    print("|          |          |          |")
    print("----------------------------------")
    print("|          |          |          |")
    print("|          |          |          |")
    print("|     {}    |     {}    |     {}    |".format(board[3], board[4], board[5]))
    print("|          |          |          |")
    print("|          |          |          |")
    print("----------------------------------")
    print("|          |          |          |")
    print("|          |          |          |")
    print("|     {}    |     {}    |     {}    |".format(board[0], board[1], board[2]))
    print("|          |          |          |")
    print("|          |          |          |")
    print("----------------------------------")


game_board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
players = {1: 'X', 2: 'O'}
turn = 0
square_selection = 0
winner = False
print(print_board(game_board))
while not winner:
    print_board(game_board)
    square_selection = int(input("Player {}, make your move\n".format(turn % 2 + 1)))
    while update_board(square_selection - 1, players[turn % 2 + 1]):
        square_selection = int(input("Try again\n".format(turn % 2 + 1)))
    if check_winner(game_board, turn % 2 + 1) != 0:
        winner = True
    turn += 1
    if turn == 9:
        print("TIE GAME")
        break

