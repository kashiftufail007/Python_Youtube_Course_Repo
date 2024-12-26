import random

'''
Rock crushes Scissors.
Scissors cuts Paper.
Paper covers Rock.

'''
print("P -> for Paper")
print("R -> for Rock")
print("S -> for Scissors")

yourChoiceStr = input("Please enter your Choice: ")

choiceDict = {"P": 1 ,"R":2 , "S":3 }
standardStr = {1: "Paper" , 2:"Rock" , 3: "Scissors" }
yourChoice = choiceDict[yourChoiceStr]
computerChoice = random.choice([1,2,3])
print(f"Your Choice: {standardStr[yourChoice]} \nComputer Choice: {standardStr[computerChoice]}")
if(computerChoice == yourChoice):
    print("DRAW")
else: 
    if(yourChoice== 2 and computerChoice ==1):
        print("You Lose                  ")
    elif (yourChoice== 3 and computerChoice ==1):
        print("You Win")
    elif (yourChoice== 1 and computerChoice ==2):
        print("You Win")
    elif (yourChoice== 3 and computerChoice ==2):
        print("You Lose")
    elif (yourChoice== 1 and computerChoice ==3):
        print("You Lose")
    elif (yourChoice== 2 and computerChoice ==3):
        print("You Win")
    else:
        print("Something went wrong!!!")

