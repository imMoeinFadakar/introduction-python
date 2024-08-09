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

user_choice = input()


print("Computer :" , computer_choice)
print("Human :" , user_choice)

if computer_choice == "rock" and user_choice == "paper":
    print("این بازی را کامل کنید")

