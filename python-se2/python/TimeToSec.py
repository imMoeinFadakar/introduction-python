
hours = float(input("Enter The Hour:")) # 1h
min = float(input("Enter The min:")) # 30m
sec = float(input("Enter The sec:")) # 2s


HourToMIn =  (hours * 60) + min
minToSec = HourToMIn * 60

print(f"your Time From Hour to Sec : {minToSec + sec} s")
