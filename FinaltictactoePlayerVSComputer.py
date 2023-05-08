import random

def playgame():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = random.choice(players)
    print_board(board)
    while True:
        if current_player == 'X':
            """
            Player's move
            """
            row, col = get_player_move(board)
            board[row][col] = current_player
        else:
            """
            Computer's move
            """
            row, col = get_computer_move(board, current_player)
            board[row][col] = current_player
            print(f"Computer plays ({row}, {col})")

        """
        Print out the game board
        """
        print_board(board)
        """
        Check if the game is over
        """
        if check_winner(board, current_player):
            print(current_player, 'wins!')
            return current_player
        elif check_tie(board):
            print('Tie!')
            return 'Tie'
        """
        Switch to the other player
        """
        current_player = players[(players.index(current_player) + 1) % 2]

def get_player_move(board):
    while True:
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter col: "))
            if board[row][col] == ' ':
                return row, col
            else:
                print("That spot is already taken, try again!")
        except (ValueError, IndexError):
            print("Invalid input, try again!")

def get_computer_move(board, player):
    """
    Simple computer move: pick a random spot that's not taken
    """
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            return row, col

def check_winner(board, player):
    """
    Check rows
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    """
    Check columns
    """
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    """
    Check diagonals
    """
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_tie(board):
    """
    Check board empty area
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True

def estimate_win_probability():
    num_trials = int(input("Enter the number of trials: "))
    wins = 0
    for i in range(num_trials):
        winner = playgame()
        if winner == 'X':
            wins += 1
    return wins/num_trials

def print_board(board):
    for row in board:
        print('|'.join(row))

print('Estimated winning probability for X:', estimate_win_probability())
