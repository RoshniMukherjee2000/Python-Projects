# game_logic.py

import random                      # Imports the random module to select a random word
from collections import Counter    # Imports Counter to count occurrences of each letter
from words import WORDS            # Imports the list of fruit names from words.py


# Function to select a random word from the list
def choose_word():
    return random.choice(WORDS)    # Returns one random fruit name from WORDS


# Main Hangman game function
def play_hangman():
    print("\n=====  Welcome to Hangman Game (Fruit Edition)  =====\n")  # Display welcome message

    word = choose_word()                 # Calls the function to get a random fruit name
    word_counter = Counter(word)         # Counts letter frequency of the selected word
    guessed = set()                      # A set to store already guessed letters
    chances = 6                          # Player is allowed 6 wrong attempts

    print("Guess the fruit name!")       # Prompt the user to guess the word
    print("_ " * len(word))              # Display underscores for each letter in the word

    # Game Loop → continues until chances become 0
    while chances > 0:
        guess = input("\nEnter a letter: ").lower()   # Take user input and convert to lowercase

        # Input validation (must be one alphabet letter)
        if len(guess) != 1 or not guess.isalpha():
            print(" Enter only one alphabet letter!")  # Show error message for invalid input
            continue                                   # Skip to next loop iteration

        # Check if letter was already guessed before
        if guess in guessed:
            print(" You already guessed this letter.")  # Notify repeated guess
            continue                                    # Skip further checks

        guessed.add(guess)                              # Add the new guessed letter to the set

        # Check if guessed letter exists in the word
        if guess in word_counter:
            print(" Correct guess!")                    # User guessed correct letter
        else:
            chances -= 1                                # Wrong guess → reduce chances
            print(f" Wrong guess! Chances left: {chances}")  # Display remaining chances

        # Display current progress of the word
        display = ""                                    # Initialize empty string to build output
        for ch in word:                                 # Loop through each letter of the word
            display += (ch + " ") if ch in guessed else "_ "  # Show letter or underscore

        print("Current Word:", display)                 # Print the updated word progress

        # Check if all letters are guessed → Player wins
        if all(ch in guessed for ch in word):
            print("\n You won! The word was:", word)    # Display win message
            return                                       # Exit the function after winning

    # If out of chances → Player loses
    print("\n Game Over! The word was:", word)          # Display losing message
