questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "New York", "Tokyo"],
        "answer": "Paris"
    },
    {
        "question": "Who is the inventor of the World Wide Web?",
        "options": ["Bill Gates", "Mark Zuckerberg", "Steve Jobs", "Tim Berners-Lee"],
        "answer": "Tim Berners-Lee"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Saturn", "Jupiter", "Mars", "Venus"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean in the world?",
        "options": ["Atlantic Ocean", "Pacific Ocean", "Indian Ocean", "Southern Ocean"],
        "answer": "Pacific Ocean"
    }
]

score = 0
for question in questions:
    print(question["question"])
    for i, option in enumerate(question["options"]):
        print(f"{i+1}. {option}")
    user_input = input("Enter your answer: ")
    if user_input.lower() == question["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is: ", question["answer"])
print("Quiz completed. Your score is: ", score)
