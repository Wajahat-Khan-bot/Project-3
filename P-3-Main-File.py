# Number guess game
import random

# Get an input and set it as end of range
while True:
    print("------------------------")
    rang = input("Enter a number: ")
    if rang.isdigit():
        rang = int(rang)
        if rang <= 0:
            print("Please enter a number bigger than 0")
        else:
            break
    else:
        print("Please write a number")
        continue

rand_num = random.randint(0, rang)

guess = 0

while True:
    print("Guess the number b/w 0 to", rang, ": ")
    intake = input("")
    guess += 1

    # Check that intake is an int or not
    if intake.isdigit():
        intake = int(intake)
        if intake == rand_num:
            print("You guess the correct number.")
            break
        elif intake <= rand_num:
            print("Your guess is smaller than actual number.")
        else:
            print("Your guess is bigger than actual number.")
    else:
        print("Please write a number")

print("You guess the correct answer in", guess, "guesses")
