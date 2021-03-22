from random import randint


def new_board(size):
    return [["O"] * size for x in range(size)]


def print_board(board):
    for row in board:
        print(" ".join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


print("Let's play Battleship!")

side = 10
board = new_board(side)
print_board(board)

ship_row = random_row(board)
ship_col = random_col(board)

turn = 0
while turn < side:
    turn += 1
    if turn < side:
        print("This is turn %d." % (turn))
    else:
        print("This is turn %d, your last turn!" % (turn))
    while True:
        try:
            guess_row = int(input("Guess Row:"))
            guess_col = int(input("Guess Col:"))
            break
        except ValueError:
            print("You have to enter a number.")
    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[ship_row][ship_col] = "W"
        print_board(board)
        break
    elif guess_row not in range(side) or guess_col not in range(side):
        print("Oops, that's not even in the ocean.")
        turn -= 1
    elif board[guess_row][guess_col] == "X":
        print("You guessed that one already.")
        turn -= 1
    else:
        print("You missed my battleship!")
        board[guess_row][guess_col] = "X"
        print_board(board)
        if turn > side - 1:
            print("Game Over.")
            print("My battleship was at Row %d, Column %d." %
                  (ship_row, ship_col))
            board[ship_row][ship_col] = "M"
            print_board(board)
