# define requirements for the list, such as what it can and cannot take
# request the list items and store them in a dictionary or list
# group in order of importance (on a sclae of 1-3)
# add ADT opperations such as editing, deleting, and updating
# users should be able to mark lists as complete or incomplete

# Create an empty dictionary to store the to-do list items
todo_list = {}

begin = input("WELCOME TO TO-DO LIST!!!\n Enter...\n 1. To add to list.\n")
while True:
    if begin == "1":
        task = input("Enter new task ")
        
        
        status = input("Enter task status (not started, in progress, done): ")
        print( "\n " + task + ": " + status )
        todo_list[task] = status
        quit = input("input q to quit:")
        if quit == 'q':
            exit()
    else:
        print("Kindly read the instructions carefully and try again\n")
        break


    


