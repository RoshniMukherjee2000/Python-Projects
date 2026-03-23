# main.py

# Import log_data and retrieve_data functions from health_manager.py
from health_manager import log_data, retrieve_data

# Import USERS dictionary from users.py
from users import USERS


# ---------------------------------------------------
# Main function that controls the entire application
# ---------------------------------------------------
def main():
    # Print application header
    print("\n===== Health Management System =====\n")

    # Display list of all available users
    print("Select User:")
    for key, name in USERS.items():  # Loop through dictionary items
        print(f"{key}. {name}")      # Example: 1. Roshni, 2. Amit

    try:
        # Ask user to choose a user number
        user_choice = int(input("\nEnter user number: "))

        # Validate if the entered user exists in USERS dictionary
        if user_choice not in USERS:
            print("Invalid user selection!")
            return  # Stop the function and return to menu loop

        # Display menu of available actions
        print("\n1. Log Exercise")
        print("2. Log Diet")
        print("3. Retrieve Exercise Log")
        print("4. Retrieve Diet Log")

        # Ask user to choose an action
        action = int(input("Enter your choice: "))

        # Match user choice to the correct function
        if action == 1:
            log_data(user_choice, "exercise")  # Log exercise details
        elif action == 2:
            log_data(user_choice, "diet")      # Log diet details
        elif action == 3:
            retrieve_data(user_choice, "exercise")  # Show exercise log
        elif action == 4:
            retrieve_data(user_choice, "diet")      # Show diet log
        else:
            print("Invalid option!")  # If user enters a wrong menu number

    except ValueError:
        # Handles case when user enters non-numeric input
        print("Please enter numeric input only!")


# ---------------------------------------------------
# Program entry point
# The code inside this block runs only when main.py is executed directly
# ---------------------------------------------------
if __name__ == "__main__":
    while True:  # Infinite loop until user chooses to exit
        main()   # Run the menu

        # Ask user if they want to continue
        again = input("Do you want to continue? (y/n): ").lower()

        # If user chooses 'n', exit the loop and end program
        if again != 'y':
            print("\nThank you for using the Health Management System!")
            break
