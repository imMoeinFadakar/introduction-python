user_list = []
count_of_entered_numbers_user = 0

i = 0
while i == 0:
    count_of_entered_numbers_user += 1
    userNumber = input(f"please enter {count_of_entered_numbers_user}th number:")

    if userNumber == "exit":
        break

    user_list.append(userNumber)


print(user_list)

sorted_user_list = sorted(user_list)

print(sorted_user_list)

if user_list == sorted_user_list:
    print("same!")
else:
    print("not same!")