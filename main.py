from todo import ToDoApp      # Import the ToDoApp class from todo.py

app = ToDoApp()               # Create an object of ToDoApp to manage tasks

while True:                   # Infinite loop to keep showing menu until user exits
    print("\n---- TO DO MENU ----")     # Display menu header
    print("1. Add Task")                 # Option 1: Add a task
    print("2. Remove Task")              # Option 2: Remove a task
    print("3. Show Tasks")               # Option 3: Display all saved tasks
    print("4. Exit")                     # Option 4: Exit the program

    choice = input("Enter choice: ")     # Take user’s menu selection

    if choice == "1":                     # If user chooses to add a task
        task = input("Enter task: ")      # Ask for task description
        app.add_task(task)                # Call method to add task

    elif choice == "2":                   # If user chooses to remove a task
        task = input("Enter task to remove: ")   # Ask task name to remove
        app.remove_task(task)                     # Call method to remove it

    elif choice == "3":                   # If user chooses to show all tasks
        app.show_tasks()                 # Display the list of tasks

    elif choice == "4":                   # If user wants to exit
        print("Exiting...")               # Print exit message
        break                             # Break loop → End program

    else:                                 # If invalid menu option entered
        print("Invalid choice! Try again.")   # Show error message
