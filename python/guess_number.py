# this is a (( guess Numb)


import math
import random

computerNumber = random.randint(20 , 40)

for i in range(100):
    userGuess = int(input("please Enter The Correct Number:"))
    if userGuess == computerNumber:
        print("you won")
        print(f"you tried {i + 1} time(s) ") # we add +1 because i started from 0
        break

    elif userGuess > computerNumber:
        print("to height!")
    elif userGuess < computerNumber:
        print("to Low!")


