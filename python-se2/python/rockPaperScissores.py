import random

user_score = 0
Computer_score = 0

random_number_Computer = random.randint(1,3)

if random_number_Computer == 1:
    computer_choice = "rock"
elif random_number_Computer == 2:
    computer_choice = "paper"
elif random_number_Computer == 3:
    computer_choice = "scissors"

i = 1

while  i :

    print("your Options:")
    print("1 . scissors")
    print("2 . paper")
    print("3 . rock")
    print("4 . exit")



    user_choice = input("Enter Your Choice :")


    if user_choice == "scissors" or user_choice == "paper" or user_choice == "rock" or user_choice == "exit":

        print("Computer :" , computer_choice)
        print("Human :" , user_choice)

        if computer_choice == "rock" and user_choice == "paper":
            user_score = user_score + 1
            print(f"user Won user: {user_score} computer: {Computer_score} ")

        elif computer_choice == "paper" and user_choice == "paper":
            print(f" Draw! user: {user_score} computer: {Computer_score} ")

        elif computer_choice == "scissors" and user_choice == "paper":
            Computer_score = Computer_score + 1
            print(f"Computer  Won ; user: {user_score} computer: {Computer_score}  ")

        elif computer_choice == "rock" and user_choice == "rock":
            print(f" Draw! ; user: {user_score} computer: {Computer_score}  ")

        elif computer_choice == "paper" and user_choice == "rock":
            Computer_score = Computer_score + 1
            print(f"Computer Won ; user: {user_score} computer: {Computer_score}  ")

        elif computer_choice == "scissors" and user_choice == "rock":
            user_score = user_score + 1
            print(f"user Won ; user: {user_score} computer: {Computer_score} ")

        elif computer_choice == "rock" and user_choice == "scissors":
            Computer_score = Computer_score + 1
            print(f"user Won ; user: {user_score} computer: {Computer_score} ")

        elif computer_choice == "paper" and user_choice == "scissors":
            user_score = user_score + 1
            print(f"user Won ; user: {user_score} computer: {Computer_score} ")

        elif computer_choice == "scissors" and user_choice == "scissors":
            print(f" Draw! user: {user_score} computer: {Computer_score} ")
        elif user_choice == "exit":
            print("thank U!")
            break
    else:
        print("please Enter a Valid Choice!")


    # 1 . scissors
    # 2 . paper
    # 3 . rock
    # 4 . exit
