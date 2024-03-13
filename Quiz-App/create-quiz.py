import json
import sys
from extra import takeInt


# Example usage:
qno = takeInt("Enter the no of quiz: ")

# myquiz = [{
#     "question": "what is the capital of india?",
#     "options":["West Bengal", "Maharashtra", "Bihar", "Delhi"],
#     "answer":"Delhi"
# }]

# Initialize an empty list to store quiz dictionaries
quizzes = []

for _ in range(qno):
    question = input("Enter the Question: ")
    answer = input("Enter the answer: ")
    options = [input(f"Enter option {i + 1}: ") for i in range(3)]

    # Create a dictionary for the current quiz
    myquiz = {
        "question": question,
        "answer": answer,
        "options": options
    }

    # Append the quiz to the list
    quizzes.append(myquiz)

# Write the list of quizzes to a JSON file
filename = input("Enter the file name (e.g., quiz.json): ")
with open(filename, "w") as outfile:
    json.dump(quizzes, outfile, indent=4)

print(f"Quiz data has been saved to {filename} in JSON format.")
