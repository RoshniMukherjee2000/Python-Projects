import random
from utils import calculate_attempts

def start_game():
    print("\n Welcome to the Number Guessing Game!")

    # Range input
    try:
        start = int(input("Enter start of range: "))
        end = int(input("Enter end of range: "))

        if start >= end:
            print("Invalid range! Start must be less than end.")
            return
    except ValueError:
        print("Invalid input! Only numbers allowed.")
        return

    secret_number = random.randint(start, end)
    attempts = calculate_attempts(start, end)

    print(f"\nI have selected a number between {start} and {end}.")
    print(f"You get {attempts} attempts to guess it!\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} → Enter your guess: "))
        except ValueError:
            print("Invalid input! Only numbers allowed.")
            continue

        if guess == secret_number:
            print("\n Correct! You guessed the number!")
            return
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")

    print("\n Out of attempts!")
    print(f" The correct number was: {secret_number}")
    print("\n Thanks for playing!")
