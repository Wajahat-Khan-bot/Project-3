# Number guess game
import random

while True:
    rang = input("Set a range by giving last number in which you guess\n")
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
    intake = input("Guess the number: ")
    guess += 1
    if intake.isdigit():
        intake = int(intake)
        if intake == rand_num:
            print("You guess the correct number.")
            break
        else:
            print("Wrong guess")
    else:
        print("Please write a number")

print("You guess the correct answer in ", guess, "guesses")
