import random

num = random.randint(1,100)
attempts = 0

print("Guess the number between 1 and 100!")

while True:
    try:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess > num:
            print("Too High!")
        elif user_guess < num:
            print("Too Low!")
        else:
            print("Yaayy!! You guessed the number.")
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Invalid input! Please enter a number.")
