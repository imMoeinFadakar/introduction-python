import random
import  math


randomNumber = random.randint(10, 40)  # a random number with random library

for i in range(10):

    userNumber = int(input())
    if randomNumber == userNumber:
        print("you won !")
        break

    elif randomNumber > userNumber:
        print("go Up baby!")

    elif randomNumber < userNumber:
        print("Go Down , Its to High ")

print("game over")
