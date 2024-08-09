import time


for i in range(3):
    password = input()
    if password == "006600":
        print("wellcome")
        print("hope you have a good day")
        break
    else:
        print("wrong password")
        time.sleep(10)



