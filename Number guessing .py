import random
number = random.randint(1, 200)
attempts = 0
print("Welcome tp number gussieng game!")
print("Guess a number btw 1 and 200")

while True:
    guess = int(input("Enter your guess number"))
    attempts += 1

    if guess < number:
        print("Too low!")
    elif guess > number :
        print("Too high!")
    else:
        print("Congratulation")
        print("You guessed the number in", attempts , "attempts.")
        break

