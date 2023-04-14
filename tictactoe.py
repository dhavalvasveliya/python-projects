import os

# Function to clear the screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the current state of the game board
def print_board(board):
    clear_screen()
    print("     |     |")
    print(f"  {board[0]}  |  {board[1]}  |  {board[2]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[3]}  |  {board[4]}  |  {board[5]}")
    print("_____|_____|_____")
    print("     |     |")
    print(f"  {board[6]}  |  {board[7]}  |  {board[8]}")
    print("     |     |")

# Function to get the player's move
def get_move(player, board):
    while True:
        move = input(f"{player}, enter a position (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Please try again.")

# Function to check if the game is over
def game_over(board):
    # Check rows for a win
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != " ":
            return True
    # Check columns for a win
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != " ":
            return True
    # Check diagonals for a win
    if board[0] == board[4] == board[8] != " " or board[2] == board[4] == board[6] != " ":
        return True
    # Check if the board is full
    if " " not in board:
        return True
    # If none of the above conditions are met, the game is not over
    return False

# Function to play the game
def play_game():
    # Initialize the board and the player
    board = [" "] * 9
    player = "X"
    # Loop until the game is over
    while not game_over(board):
        print_board(board)
        move = get_move(player, board)
        board[move] = player
        player = "O" if player == "X" else "X"
    # Game is over, print the final board
    print_board(board)
    # Determine the winner or declare a tie
    if " " not in board:
        print("It's a tie!")
    else:
        winner = "X" if player == "O" else "O"
        print(f"{winner} wins!")

# Example usage:
play_game()
