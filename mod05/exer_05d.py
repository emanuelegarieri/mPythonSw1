import random

number = random.randint(1, 10)

while True:
    guess = input("Try to guess the number: ")
    if guess == "":
        break
    guess = int(guess)
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("Correct!")
        break