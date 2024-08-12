
Sec = int(input("Enter The Sec:"))

SecToMin = Sec / 60
MinToHours = SecToMin / 60

RemainMin = SecToMin % 60
RemainSec = Sec % 60

print(MinToHours)
print(RemainMin)

print(f" Time: {int(MinToHours)}:{int(RemainMin)}:{RemainSec}")