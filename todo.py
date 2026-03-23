# Import the Storage class which handles saving/loading tasks
from storage import Storage

# Define the ToDoApp class
class ToDoApp:
    
    # Constructor method to initialize the ToDoApp object
    def __init__(self):
        # Load existing tasks from storage into a list
        self.tasks = Storage.load_tasks()

    # Method to add a new task
    def add_task(self, task):
        self.tasks.append(task)              # Add the new task to the list
        Storage.save_tasks(self.tasks)       # Save updated tasks to storage
        print(f"Task added: {task}")         # Confirm task addition to user

    # Method to remove a task
    def remove_task(self, task):
        if task in self.tasks:               # Check if task exists
            self.tasks.remove(task)          # Remove task from list
            Storage.save_tasks(self.tasks)   # Save updated tasks to storage
            print(f"Task removed: {task}")   # Confirm removal to user
        else:
            print("Task not found!")         # Inform user if task does not exist

    # Method to display all tasks
    def show_tasks(self):
        if not self.tasks:                   # Check if task list is empty
            print("No tasks found.")         # Inform user if no tasks exist
        else:
            print("\nYour Tasks:")           # Header for task list
            for i, t in enumerate(self.tasks, 1):  # Enumerate tasks starting from 1
                print(f"{i}. {t}")           # Print each task with its number
