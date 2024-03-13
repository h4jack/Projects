import json
from random import randint as ri
from extra import takeInt

f = open("who.json",)

data = json.load(f)
qlen = len(data)-1
idx = 0

# idx = ri(0,qlen)
# question = data[idx]["question"]
# answer = data[idx]["answer"]
# options = set(data[idx]["options"])
# options.add(data[idx]["answer"])
# qlen -= 1

# print(question)
# print(answer)
# print(options)
# print(idx)
# print(qlen)
# print(type(question))

quizzes = data

cans = []
uans = []

i = 1
while qlen != -1:
    idx = ri(0,qlen)
    question = data[idx]["question"]
    answer = data[idx]["answer"]
    options = set(data[idx]["options"])
    options.add(data[idx]["answer"])
    
    print(f"1. Question: ",question)
    # print("Answer : ", answer)
    option_list = list(options)
    print("1. Optioins: ")
    j = 1
    for option in option_list:
        print(f"\t{j}. {option}")
        j += 1
    ans = takeInt("Enter the answer e.g: 3 : ", 1, 4)
    if option_list.index(answer)+1 == ans:
        print("Currect Answer.")
    else:
        print("Wrong Answer.")
    
    data.pop(idx)
    qlen -= 1
    i += 1
