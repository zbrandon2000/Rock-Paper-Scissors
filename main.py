import random

question_1 = (input("Hi, would you like to play rock, paper, scissors?"))

option1 = "yes"

option2 = "no"

if question_1 == option2:
    print("BYE!!")
    
CPUoptions = ["rock", "paper", "scissors"]

# while u need to make theis x paprt rockets forever and hiihi misery
if question_1 == option1:
    print("Rock, paper, scissors, shoot!")
    random_choice = random.randint(0, 2)
    CPUchoice = CPUoptions[random_choice]
    result = None
    yourchoice = input("What is your choice, Rock, paper, or scissors?")
    print(CPUchoice)
    if yourchoice == CPUchoice:
        print("It's a tie!. Again!")

    elif (yourchoice == "rock" and CPUchoice == "scissors") or (yourchoice == "paper" and CPUchoice == "rock") or (yourchoice == "scissors" and CPUchoice == "paper"):
       
        print("YOU WIN YAYYYYYYYYYY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    else:
        print("YOU LOSE HA HA"ddd)
