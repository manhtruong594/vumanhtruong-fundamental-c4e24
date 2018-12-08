q1 = {
    "question" : "If x = 8, then what is the value of 4(x + 3) ?",
    "answer" : {
            "1. " : 35,
            "2. " : 36,
            "3. " : 40,
            "4. " : 44,
        },
    "correct_answer" : 4
}

q2 = {
    "question" : "Estimate this answer (exact calculation not needed): /n Jack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean?",
    "answer" : {
            "1. " : "About 55",
            "2. " : "About 65",
            "3. " : "About 75",
            "4. " : "About 85"
        },
    "correct_answer" : 2
} 

print("Answer the following algebra question: ")

questions_list = [q1, q2]

for i in range(len(questions_list)):
    print(questions_list[i]["question"])
    print(questions_list[i]["answer"])
    while True:
        ur_answer = input("Your answer? ")
        if int(ur_answer) == questions_list[i]["correct_answer"]:
            print("Bingo")
            print()
            break
        else:
            print("Sorry :(, choose another answer!! ")