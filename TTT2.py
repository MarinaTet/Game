#TTT2 - HW les6
import random

def evaluate(board):
    if 'xxx' in board:
        return 'x'  # Player wins
    elif 'ooo' in board:
        return 'o'  # PC wins
    elif '-' not in board:
        return '!'  # Draw
    else:
        return '-'  # Game is still ongoing

def move(board, mark, position):
    board_list = list(board)  # Convert string to list for mutability
    board_list[position] = mark  # Place the mark at the specified position
    return ''.join(board_list)  # Convert back to string

def player_move(board):
    while True:
        try:
            position = int(input("Enter your move (0-19): "))
            if position < 0 or position > 19:
                print("Invalid position! Please choose a number between 0 and 19.")
            elif board[position] != '-':
                print("Position already occupied! Try another.")
            else:
                return move(board, 'x', position)  # Place player's mark
        except ValueError:
            print("Invalid input! Please enter a number.")

def pc_move(board):
    while True:
        position = random.randint(0, 19)  # Generate a random position
        if board[position] == '-':  # Check if the position is empty
            return move(board, 'o', position)  # Place the computer's mark

def tictactoe_1d():
    board = "--------------------"  # Initialize an empty board
    print("Welcome to 1D Tic-Tac-Toe!")
    
    while True:
        print("Current board:", board)
        
        # Player's turn
        board = player_move(board)
        status = evaluate(board)
        if status == 'x':
            print("Congratulations! You win!")
            break
        elif status == '!':
            print("It's a draw!")
            break
        
        print("Current board:", board)

        # PC's turn
        board = pc_move(board)
        status = evaluate(board)
        if status == 'o':
            print("Computer wins! Better luck next time.")
            break
        elif status == '!':
            print("It's a draw!")
            break

# Run the game
tictactoe_1d()
