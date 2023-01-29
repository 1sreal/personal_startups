import random

def guess_the_number():
    print("Guess the Number Game")
    print("-------------------\n")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    
    while True:
        # Get player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
       