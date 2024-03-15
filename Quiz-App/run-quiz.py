import json
from random import randint as ri
from extra import takeInt
from sys import argv
from os.path import exists
from os import remove

if(len(argv) > 1):
    f = open(argv[1])
else:
    f = open(input("Enter the file name : "),)
data = json.load(f)
answered = []

def take_quiz():
    quizzes = list(data)
    qlen = len(quizzes)-1
    i = 1
    while qlen != -1:
        idx = ri(0,qlen)
        question = quizzes[idx]["question"]
        answer = quizzes[idx]["answer"]
        options = set(quizzes[idx]["options"])
        options.add(quizzes[idx]["answer"])
        
        print(f"{i}. Question: {question}")
        # print("Answer : ", answer)
        option_list = list(options)
        print("1. Optioins: ")
        j = 1
        for option in option_list:
            print(f"\t{j}. {option}")
            j += 1
        ans = takeInt("Enter the answer e.g: 3, or 0 to skip : ",0 , 4)
        if(ans != 0):
            if option_list.index(answer)+1 == ans:
                print("Currect Answer.")
            else:
                print("Wrong Answer.")
            answered.append(quizzes[idx])
            answered[-1]["options"] = option_list
            answered[-1]["given_answer"] = option_list[ans-1]
        else:
            print("Skipped...")
        quizzes.pop(idx)
        qlen -= 1
        i += 1
    total_question = len(data)
    total_answered = len(answered)
    total_skipped = total_question-total_answered
    print(total_question)
    print(total_answered)
    print(total_skipped)

    save_file = (input("enter y/es to save your answers on a file : ") in ['y','yes'])
    if(save_file):
        result_file = input("Enter the file name without .json : ")
    else:
        result_file = "temp"
    i = 0
    result_file_path = result_file+".json"
    while(exists(result_file_path)):
        result_file_path = result_file+"_"+f"{i}"+".json"
        i += 1
    result_file = result_file_path
    del result_file_path

    if(save_file):
        with open(result_file, "w") as outfile:
            json.dump(answered, outfile, indent=4)

        print(f"Quiz  has been saved to {result_file} in JSON format.")
    else:
        os.remove(result_file)

    if(input("enter y/es to print the result : ") in ['y','yes']):
        print_result(result_file)

def print_result(result):
    if(type(result) == str):
        if(exists(result)):
            f = open(result)
            result = json.load(f)
        else:
            print("file doesn't exists...")
    elif(type(result) != dict):
        print("argument is not a valid type..")
        return
    i = 1
    for questions in result:
        print(f"{i}. Question: {questions["question"]}")
        print("Options: ")
        j = 1
        for option in questions["options"]:
            print(f"{j}. {option}")
            j+=1
        print(f"Given Answer: {questions["given_answer"]}")
        print(f"Currect Answer: {questions["answer"]}")
        print()
        i+=1


if __name__ == '__main__':
    take_quiz()