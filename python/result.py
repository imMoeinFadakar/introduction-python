print("Enter first degree")
firstNumber = float(input())

print("Enter second degree")
secondNumber = float(input())

print("Enter Third degree")
ThirdNumber = float(input())


allDegrees = firstNumber + secondNumber + ThirdNumber

result = allDegrees / 3
print(f" result = {result}")

if result < 12:
    print(f" result = {result} status: fail")

elif result > 12 and result < 17:
    print(f" result = {result} status: normal")

elif result > 17 and result < 20:
    print(f" result = {result} status: Great")



