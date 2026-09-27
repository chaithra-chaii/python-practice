import random

choices = ["stone", "paper", "scissor"]

user = input("Enter your choice [stone/paper/scissor]: ").lower()
computer = random.choice(choices)

print("Your choice:", user)
print("Computer's choice:", computer)

if user == computer:
    print("Result: Draw")
elif (user == "stone" and computer == "scissor") or \
     (user == "scissor" and computer == "paper") or \
     (user == "paper" and computer == "stone"):
    print("Result: You win!")
else:
    print("Result: Computer wins!")
