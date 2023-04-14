# Define the game board as a list of empty strings
board = [" " for _ in range(9)]

# Function to print the game board
def print_board():
    print("|".join(board[0:3]))
    print("-+-+-")
    print("|".join(board[3:6]))
    print("-+-+-")
    print("|".join(board[6:9]))

# Function to check if a player has won
def check_win(player):
    # Define the winning combinations as tuples of the board indices
    wins = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    # Check if any of the winning combinations are all occupied by the player's symbol
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to play the game
def play_game():
    # Define the players and their symbols
    players = ["X", "O"]
    # Define the index of the current player
    current_player = 0
    
    # Loop until the game is over
    while True:
        print_board()
        # Prompt the current player to make a move
        move = input(f"Player {current_player+1}, enter your move (1-9): ")
        # Convert the move to a board index
        index = int(move) - 1
        # Check if the move is valid (i.e., the board index is empty)
        if board[index] == " ":
            # Place the player's symbol on the board
            board[index] = players[current_player]
            # Check if the player has won
            if check_win(players[current_player]):
                print_board()
                print(f"Player {current_player+1} wins!")
                return
            # Check if the board is full (i.e., the game is a tie)
            elif all(square != " " for square in board):
                print_board()
                print("It's a tie!")
                return
            # Switch to the other player
            current_player = 1 - current_player
        else:
            print("Invalid move. Try again.")

# Play the game
play_game()
