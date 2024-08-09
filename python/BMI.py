print("Enter your Weight")
weight = float(input())

print("Enter Your Height (m)")
height = float(input())

result = weight / (height ** 2)

print(result)

if result < 18.5:
    print("status: UnderWeight")
elif result < 24.9 and result > 18.5:
    print("status: Normal Weight")
elif result > 24.9 and result < 30:
    print("status: Over Weight")
elif result > 30 and result < 35:
    print("status: Obesity")
elif result > 35 and result < 42:
    print("status: Extreme Obesity")