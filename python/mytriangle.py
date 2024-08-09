import math

print("Enter The First Side")
firstSide = float(input())

print("Enter The Second Side")
SecondSide = float(input())

print("Enter The Third Side")
ThirdSide = float(input())

if (firstSide + SecondSide) < ThirdSide:
    print("no , its not possible")
elif (ThirdSide + SecondSide) < firstSide:
    print("no , its not possible")
elif (ThirdSide + firstSide) < SecondSide:
    print("no , its not possible")
else:
    print("yes its Possible")