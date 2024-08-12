import random

i=1
while i:

    dice = random.randint(1,6)

    if dice != 6:
        print(f"score:{dice}")
        break
    else:
        print("WOO! Its 6 Try agine!")
