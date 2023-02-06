# define requirements for the list, such as what it can and cannot take
# request the list items and store them in a dictionary or list
# group in order of importance (on a sclae of 1-3)
# add ADT opperations such as editing, deleting, and updating
# users should be able to mark lists as complete or incomplete

# Create an empty dictionary to store the to-do list items
todo_list = {}

begin = input("WELCOME TO TO-DO LIST!!!\n Enter 1. To add to list.\n 2. To view list.\n q. To quit. ")
while begin == "1":
    input("Enter task (q to quit):")
    if task == 'q':
        break
     
    status = input("Enter task status (not started, in progress, done): ")
    todo_list[task] = status
while begin == "2":
    print(todo_list)
    

