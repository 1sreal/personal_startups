import random

def guess_the_number():
    print("Guess the Number Game")
    print("-------------------\n")
    
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    attempts = 0
    
    # Determine two clues for the number
    if number % 2 == 0:
        clue1 = "even"
    else:
        clue1 = "odd"
        
    if number >= 1 and number <= 50:
        clue2 = "between 1 and 50"
    else:
        clue2 = "between 51 and 100"
        
    while True:
        # Get player's guess
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        # Check player's guess
        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("You got it in", attempts, "attempts!")
            print("The number was", clue1, "and", clue2)
            play_again = input("Would you like to play again? (yes/no) ")
            
            # Use a switch case to handle user's answer
            switch_play_again = {
                "yes": True,
                "no": False
            }
            
            if switch_play_again.get(play_again.lower()):
                guess_the_number()
            else:
                break

# Start the game
guess_the_number()
