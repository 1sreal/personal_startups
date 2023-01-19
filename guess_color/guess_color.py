riddles = {
    "I am the color of the sky and the ocean. What am I?": "blue",
    "I am the color of a stop sign. What am I?": "red",
    "I am the color of grass. What am I?": "green",
    "I am the color of a banana. What am I?": "yellow",
    "I am the color of a flamingo. What am I?": "pink",
    "I am the color of a cloud. What am I?": "white",
    "I am the color of coal. What am I?": "black",
    "I am the color of a pumpkin. What am I?": "orange",
    "I am the color of a peacock. What am I?": "blue",
    "I am the color of a cherry. What am I?": "red"
}

score = 0

for riddle, answer in riddles.items():
    guess = input(riddle + " ")
    if guess.lower() == answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The answer is " + answer + ".")

print("You got " + str(score) + " out of " + str(len(riddles)) + " correct.")
