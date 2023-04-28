# Vince-Mistake

# Define the board as a list of 9 empty strings
board = [""] * 9

# Define the function to check if there is a winning combination
def is_victory(symbol):
    return (board[0] == symbol and board[1] == symbol and board[2] == symbol) or \
           (board[3] == symbol and board[4] == symbol and board[5] == symbol) or \
           (board[6] == symbol and board[7] == symbol and board[8] == symbol) or \
           (board[0] == symbol and board[3] == symbol and board[6] == symbol) or \
           (board[1] == symbol and board[4] == symbol and board[7] == symbol) or \
           (board[2] == symbol and board[5] == symbol and board[8] == symbol) or \
           (board[0] == symbol and board[4] == symbol and board[8] == symbol) or \
           (board[2] == symbol and board[4] == symbol and board[6] == symbol)

# Define the function to print the board
def show_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Define the function to check if the game is over
def is_game_over():
    # Check if there is a winning combination
    if is_victory("X") or is_victory("O"):
        return True
    # Check if the board is full
    if "" not in board:
        return True
    # Game is not over
    return False

# Define the main game loop
def play_game():
    player = "X"
    while not is_game_over():
        show_board()
        move = int(input(f"{player}'s turn. Enter a number from 1-9 to make a move: ")) - 1
        if board[move] == "":
            board[move] = player
            # Switch to the other player
            player = "O" if player == "X" else "X"
        else:
            print("That space is already taken. Try again.")
    # Game is over, print the final board
    show_board()
    if is_victory("X"):
        print("X wins!")
    elif is_victory("O"):
        print("O wins!")
    else:
        print("It's a tie!")

# Start the game
play_game()
