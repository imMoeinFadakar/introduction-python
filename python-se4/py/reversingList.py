from audioop import reverse

user_list = []

i = 1
while i:
    user_entered_number = input("enter number > 0 or exit for end") # we got the user numbers

    if user_entered_number == "exit": # check if user entered exit in input the loop will be break
        print("your numbers saved, good luck !")
        break
    else:
        if int(user_entered_number) < 0: # Entered number most be more than 0
            print("Error: nagetive cant be exist in this list")
        else:
            user_list.append(user_entered_number)


print(f"your original list:, {user_list}")
user_list.reverse()
print(f"your reversed list : {user_list}")