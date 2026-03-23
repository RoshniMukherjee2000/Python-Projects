# Import the os module to check for file existence
import os

# Define the Storage class to handle saving and loading tasks
class Storage:
    # Name of the file where tasks will be stored
    FILE_NAME = "tasks.txt"

    # Static method to load tasks from the file
    @staticmethod
    def load_tasks():
        """Load tasks from file and return a list"""
        # If the file does not exist, return an empty list
        if not os.path.exists(Storage.FILE_NAME):
            return []

        # Open the file in read mode
        with open(Storage.FILE_NAME, "r") as file:
            # Read all lines, strip newline characters, and store in a list
            tasks = [line.strip() for line in file.readlines()]
        # Return the list of tasks
        return tasks

    # Static method to save a list of tasks into the file
    @staticmethod
    def save_tasks(tasks):
        """Save the list of tasks into the file"""
        # Open the file in write mode (overwrites existing content)
        with open(Storage.FILE_NAME, "w") as file:
            # Write each task in the list to a new line in the file
            for task in tasks:
                file.write(task + "\n")
