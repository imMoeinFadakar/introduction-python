def factorial(n): # this function will check the number its factorial or not
    i = 1
    while i <= n:
        if n % i == 0:
            n //= i
        else:
            return False
        i += 1
    return n == 1

number = int(input("Enter a number: "))
if factorial(number):
    print(f"{number} is a factorial.")
else:
    print(f"{number} is not a factorial.")