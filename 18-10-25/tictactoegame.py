# Tic Tac Toe Game in Python

# Function to display the board
def print_board(board):
    print("\n")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print("\n")

# Function to check for a win
def check_winner(board, player):
    win_conditions = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Main game function
def tic_tac_toe():
    board = [' '] * 9  # 3x3 board
    current_player = 'X'

    for turn in range(9):
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Take input
        move = int(input("Enter a position (1-9): ")) - 1
        
        # Check if position is available
        if board[move] != ' ':
            print("Position already taken! Try again.")
            continue
        
        # Update board
        board[move] = current_player
        
        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            return
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'
    
    print_board(board)
    print("It's a draw!")

# Run the game
tic_tac_toe()