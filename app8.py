#quiz program

#create a dictionary that stores questions and answers 
#create variables that track the score of the player 
#loop through the dict using the key value pairs amnd show the questions to the users
#Gather their response 
#prompt them if they're right or wrong
#show the user answer at the end of the quiz 

quiz = {
    "question1": {
        "question": "What is the capital of Argentina",
        "answer": "Buenos Aires"
    },
    "question2": {
        "question": "What is the capital of Germany",
        "answer": "Berlin"
    },
    "question3": {
        "question": "What is the capital of Egypt",
        "answer": "Cairo"
    },
    "question4": {
        "question": "What is the capital of England",
        "answer": "London"
    },
    "question5": {
        "question": "What is the capital of Spain",
        "answer": "Madrid"
    },
    "question6": {
        "question": "What is the capital of Austria",
        "answer": "Vienna"
    },
    "question7": {
        "question": "What is the capital of Hungary",
        "answer": "Budapest"
    }
}

score = 0 
percentage = 0

for key,value in quiz.items():
    print(value["question"])
    answer = input("Answer?: ").lower()

    if answer == value["answer"].lower():
        score = score + 1
        print(f"Your score is {score}")
    else:
        print(f"Wrong answer, the correct answer is {value['answer']}")

print(f"your final score is {score}")
print(f"your percentage is {int((score/7)*100)} %")

