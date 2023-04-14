import random

# Function to select a random word from a list of words
def get_word():
    words = ["apple", "banana", "cherry", "orange", "peach"]
    return random.choice(words)

# Function to initialize the game board
def init_board(word):
    board = ["_"] * len(word)
    return board

# Function to print the current state of the game board
def print_board(board, guesses):
    print(" ".join(board))
    print(f"Guesses: {', '.join(guesses)}")

# Function to get the player's guess
def get_guess(guesses):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha() and guess not in guesses:
            return guess
        else:
            print("Invalid guess. Please try again.")

# Function to update the game board with the player's guess
def update_board(word, board, guess):
    for i in range(len(word)):
        if word[i] == guess:
            board[i] = guess

# Function to check if the game is over
def game_over(word, board, guesses):
    if "_" not in board:
        print(f"Congratulations, you guessed the word '{word}'!")
        return True
    elif len(guesses) == 6:
        print(f"Sorry, you ran out of guesses. The word was '{word}'.")
        return True
    else:
        return False

# Function to play the game
def play_game():
    word = get_word()
    board = init_board(word)
    guesses = []
    print("Welcome to Hangman!")
    # Loop until the game is over
    while not game_over(word, board, guesses):
        print_board(board, guesses)
        guess = get_guess(guesses)
        guesses.append(guess)
        if guess in word:
            update_board(word, board, guess)
        else:
            print(f"Sorry, '{guess}' is not in the word.")
    # Game is over, print the final board
    print_board(board, guesses)

# Example usage:
play_game()