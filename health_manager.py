# health_manager.py

# Import datetime class to get current date and time
from datetime import datetime

# Import USERS dictionary from users.py to map user numbers to names
from users import USERS


# ---------------------------------------------------
# Function: get_time()
# Purpose: Returns the current date and time as a formatted string
# ---------------------------------------------------
def get_time():
    # Format: YYYY-MM-DD HH:MM:SS
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


# ---------------------------------------------------
# Function: get_filename()
# Purpose: Creates a filename for a user's activity log
# Example output: Roshni_exercise.txt
# ---------------------------------------------------
def get_filename(user, activity):
    # USERS[user] = user name (e.g., Roshni)
    # activity = "exercise" or "diet"
    return f"{USERS[user]}_{activity}.txt"


# ---------------------------------------------------
# Function: log_data()
# Purpose: Logs diet or exercise details into a text file
# ---------------------------------------------------
def log_data(user, activity):
    # Determine filename using helper function
    filename = get_filename(user, activity)

    # Ask user to type the exercise/diet entry
    entry = input(f"Enter {activity} details: ")

    # Open the file in append mode so new data is added at the end
    with open(filename, "a") as file:
        # Write timestamp + user entry to file
        file.write(f"[{get_time()}] - {entry}\n")

    # Confirm successful logging to the user
    print(f"Successfully logged {activity} for {USERS[user]}!\n")


# ---------------------------------------------------
# Function: retrieve_data()
# Purpose: Displays stored exercise/diet data from the file
# ---------------------------------------------------
def retrieve_data(user, activity):
    # Get the correct filename for this user and activity
    filename = get_filename(user, activity)

    try:
        # Try opening the file in read mode
        with open(filename, "r") as file:
            data = file.read()

        # Display the user's activity log
        print(f"\n {USERS[user]}'s {activity.capitalize()} Log:")
        print("---------------------------------------")
        # Print log contents, or message if file empty
        print(data if data else "No records found.")
        print("---------------------------------------\n")

    except FileNotFoundError:
        # Error occurs if user has no log file yet
        print("\n No log file found! No data recorded yet.\n")
