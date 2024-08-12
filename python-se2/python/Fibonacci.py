def fib(i):
    first , Second = 0, 1
    for i in range(i):
        print(first)
        first , Second = Second , first + Second


UserNumber = int(input("enter The Count Of F :"))
fib(UserNumber)