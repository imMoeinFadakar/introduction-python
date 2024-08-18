import  math

print("hi wellcome to my calculator")
print("select One")
print("plus:+")
print("min:-")
print("mul:*")
print("div:/")
print("sqrt: sqrt")
print("sin : sin")
print("cos : cos")
print("tan : tan")
print("cot : cot")
print("factorial : fact")
print("exit : exit")



i = 1

while i == 1:
print("Select an  Operation :")
operationChoice = input()

    if operationChoice == "+" or operationChoice == "-" or operationChoice == "*" or operationChoice == "/":

        print("Now , Enter Your First Number: type 'exit' for leave ! ")
        firstNumber = input()
        if firstNumber == "exit":
            break
        else:
            firstNumber = int(firstNumber)
            print("Then , Enter Your Second Number ")
            SecondNumber = float(input())

            if operationChoice == "+":
                result = firstNumber + SecondNumber
                print("result =", result)

            elif operationChoice == "-":
                result = firstNumber - SecondNumber
                print("result =", result)

            elif operationChoice == "*":
                result = firstNumber * SecondNumber
                print("result =", result)

            elif operationChoice == "/":
                result = firstNumber / SecondNumber
            print("result =", result)



    elif operationChoice == "sqrt":
        print("Enter Your Number : sqrt , type 'exit' for leave ! ")
        userNumber = float(input())

        if userNumber < 0:
            print("Enter a Number More than 0 ")
        else:
            result = math.sqrt(userNumber)

            print(f" sqrt({userNumber})  = {result} " )

    elif operationChoice == "sin":
        print("Enter Your Number : sin , type 'exit' for leave ! ")
        userNumber = float(input())

        if userNumber < 0:
            print("please enter a number more than 0")
        else:
            radiaToDegree = math.radians(userNumber)
            result = math.sin(radiaToDegree)

            print(f" sin({userNumber}) = {result}")

    elif operationChoice == "cos":
        print("Enter Your Number : cos , type 'exit' for leave ! ")
        userNumber = float(input())
        if userNumber < 0:
            print("select a number more than 0")
        else:
            result = math.cos(userNumber)

            print(f" cos({userNumber}) = {result} ")

    elif operationChoice == "tan":
        print("Enter Your Number : tan , type 'exit' for leave ! ")
        userNumber = float(input())
        if userNumber < 0:
            print("Enter a Number More Than 0")
        else:
            radianToDegree = math.radians(userNumber)
            result = math.tan(radianToDegree)

            print(f" tan({userNumber}) = {result} ")
    elif operationChoice == "cot":
        print("Enter Your Number : cot , type 'exit' for leave ! ")
        userNumber = float(input())
        if userNumber < 0:
            print("Enter a Number More Than 0")
        else:
            def cot(num):
                return 1 / math.tan(num)

            degreeToRadian = math.radians(userNumber)
            print(F"cot({userNumber}) = {cot(degreeToRadian)}")

    elif operationChoice == "fact":
        print("Enter Your Number : factorial , type 'exit' for leave ! ")
        userNumber = input()
        IntUserNumber = int(userNumber)
        if IntUserNumber < 0:
            print("Enter a Number More Than 0")
        else:
            result = math.factorial(IntUserNumber)
            print(f" factorial({userNumber}) = {result}")


    else:
        print("operation is not valid")
        break


print("Thanks for choice Us")
