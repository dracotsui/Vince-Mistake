# Documentation of absorption
## Absorption

Construct a programme to calculate the probability that the first player will win in the game of Tic-Tac-Toe that against player 2 a number of play times. ( sample size = 10,000)

## Tutorial 

In this tutorial, we will introduce the board Tac-Tic-Toe and to estimate the probability of winning for the first player. 
 
First of all, the board of the Tic-Tac-Toe game contain the mathematical topic of matrix as the structure is a 3x3 matrices.

Given a matrix $X$ defined by:
$$
X = \begin{pmatrix}
   A & B & C\\
   D & E & F\\
   G & H & I
   \end{pmatrix}
$$
The board of tic tac toe is numbered as follows:

| 1 | 2 | 3 |
|---|---|---|
| 4 | 5 | 6 |
| 7 | 8 | 9 |

where $A,B,C,D,E,F,G,H,I$ in the martrix $X$ are equal to the board that the range of 1-9 in Tic-tac-Toe respectively.


For the beginning of creating the game, we will need to import random and def playgame().
 The starting players are randomly chosen, giving Players 1 and 2 equal chances of being the first participant. The game then continues with the player making random movements and appearing in the terminal.
```python
import random

def  playgame():
     board = [[' ']*3 for _ in range(3)]
```


 Players then begin the game by randomly placing marks on the board. Depending on whether a player has won or the game has concluded in a tie, the method then returns a winner or a tie. 

The game's outcome (a win or a tie) is then determined by the two functions (check_winner() and check_tie()), which were later defined. The check_winner() function searches for winning circumstances in columns, rows, and diagonals. The check_tie() function searches for board vacancies. However, we have additionally added and defined the method print.board() in order to print the game board's current state and gameplay.

The function estimate_win_probability(num_trials), which will run playgame() about 10000 times, is the last one we built. By counting the number of times "X" has triumphed, it will determine the likelihood that "X" will win and:

  Number of victories overall / Total games played  
 
 Since a larger sample size yields a more trustworthy result, the probability is typically around 0.43.  Is this written by you 

The tic tac toe Python library is created on a 3x3 board, where two players take turns placing their symbols (X or O) on the board. Different players will get their own symbol, a mark will either be X and O( Though most often, first player will be 0 and the second player will be X) . Win, lose and draw will depend on  whether the player can get a combination by their three symbols in this game's row, column or diagonal and we will take about this more precisely later. 

### **How to play**
This code will focus on **estimating** the probability of winning; you can fill in the number to decide how many times the computer has to try to run the match of tic tac toe. for example if you fill in the value of 1000, the `estimate_win_probability()`prompts the user to enter the number of trials they want to run using the input() function. 

## How to guides
### How to create the board of 3x3 Tic-Tac-Toe 
Initializes 3x3 game board and chooses which player starts first, randomly. The game then continues with the player making random movements and appearing in the terminal.
```python
def playgame():
   board = [[' ']*3 for _ in range(3)]
```
### How to create player
```python                         
players = ['X', 'O']                                                                      
current_player = random.choice(players)
```
### How to check win
Checks if the player won the game by checking all possible winning combinations on the game board.
```python
def check_winner(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False
```
### How to check tie
Checks if the game ends in a tie by checking if there are any empty spaces on the game board.
```python
def check_tie(board):
    # Check board empty area: 
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return False
    return True
```
### Check: win, lose or Draw
The game will be ended when three case from the board have been shown, the checking of win probability will depend on check_winning and check_tie. For `check_winning`, `check_tie`. `check_winning` function takes in the current state of the board and X or O the we want to check for a win, it will returns to `True` if the player has won, and `False` for the second case, lose. here are the detail of these three case:

1. By checking each row, column and diagonals of the board to see if all positions in the row, column and diagonals are occupied. If this is the case, then the player has won horizontally, vertically and diagonally, the function returns True. Here are how the code which will return to `True` are look like:
   -  Rows, for i = Rows:
   ```python
    if board[i][0] == board[i][1] == board[i][2]==player:
      ```
   It means that, for the range of i, if all value in a row are equal to the player, for instance: 
   ```python
   board[0][0] == board[0][1] == board[0][2]
   ```
   , the function will return to True
   
   -  Column, for j = column:
   ```python
   if board[0][j] == board[1][j] == board[2][j] == player:
      ```
   It means that, for the range of j, if all value in a column are equal to the player, for instance:
     ```python
   board[0][0] == board[1][0] == board[2][0]
   ```
   , the function will return to True
   
   -  For digonals, since there are only two case, so we do not have to use i and j to run the function, herr are the two case of digonals:
   ```python
   if board[0][0] == board[1][1] == board[2][2] == player:
   ```
   and
   ```python
   if board[0][2] == board[1][1] == board[2][0] == player:
   ```
   the function will return to True 

2. For `check_tie`, we use 
   - `if board[i][j] == ' ':` and return `False` for checking if the board is empty.

### How to estimate the probability winning 
Find the probability of player X winning the game given the specified number of trials. It calls the playgame() function the specified number of times and keeps track of how many times player X has won. By dividing the number of X wins by the total number of trials to calculate the estimated probability of winning.
```python
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
```
Then you can fill in the number to decide how many times the computer has to try to run the match of tic tac toe. for example if you fill in the value of 1000, the `estimate_win_probability()`prompts the user to enter the number of trials they want to run using the input() function. 
```python
print('Estimated winning probability for X:', estimate_win_probability())
```

## Explanation



### Overview of the probability that the first player will win in the game of Tic-Tac-Toe that against itself a number of play times

## Reference



## ** A match with Computer (Testing)
A game featuring competing with a computer programme. 
