# Number guess game
import random

rang = int(input("Set a range by giving last number in which you guess\n"))

if rang.isdigit():
    rand_num = random.randint(0, rang)
else:
    print("Please write an integer")


print(rand_num)
