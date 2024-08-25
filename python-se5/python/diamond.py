from functions import functions

number = int(input("please Enter The number for The range of Diamond:")) # taking nuber from user


if (number % 2) == 0: # check for odd or even

    print("for balance of Diamond pattern please Enter an odd number :)) ")
    exit()
else:
    functions.diamond(number)
    functions.bye()







