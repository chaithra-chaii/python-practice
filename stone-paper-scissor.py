import random

choices = ["stone", "paper", "scissor"]

user = input("Enter your choice[stone/paper/scissor]: ")
computer = random.choice(choices)

print("User's choice:",user)
print("Computer's choice:", computer)

if user == computer:
    print("Its a Draw")
elif (user == "stone" and computer == "scissor"):
    print("You Win!!")
elif (user == "scissor" and computer == "paper"):
    print("You Win!!")
elif (user == "paper" and computer == "stone"):
    print("You win!!")
else:
    print("Computer wins!!")
