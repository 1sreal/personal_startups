# define requirements for the list, such as what it can and cannot take
# request the list items and store them in a dictionary or list
# group in order of importance (on a sclae of 1-3)
# add ADT opperations such as editing, deleting, and updating
# users should be able to mark lists as complete or incomplete

# Create an empty dictionary to store the to-do list items
# Create an empty dictionary to store the to-do list items
todo_list = {}

begin = input("WELCOME TO TO-DO LIST!!!\n Enter...\n 1. To add to list.\n")
while True:
    if begin == "1":
        task = input("Enter new task ")

        allowed_statuses = ["not started", "in progress", "done"]
        status = input("Enter task status (not started, in progress, or done): ")

        if status in allowed_statuses:
            todo_list[task] = status
            print("\n" + task + ": " + status)
        else:
            print("Invalid status. Please enter only 'not started', 'in progress', or 'done'.")

        # Print all the tasks and statuses
        print("\nCurrent To-Do List:")
        for key, value in todo_list.items():
            print(key + ": " + value)
        
        quit = input("\nInput 'q' to quit, or enter  add another task: ")
        if quit == 'q':
            exit()
    else:
        print("Kindly read the instructions carefully and try again\n")
        break
