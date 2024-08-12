
degree = 0
i = 0

x = 1

while x:


   userEnter = input("Enter Your Degree`s: Enter 'exit' for quit :")
   if userEnter == "exit":
      print(f"thank U !")
      break

   i = i + 1
   degree = degree + int(userEnter)
   print(f"average = {degree / i}")
   print(f" Count Of YOur Lessons: {i}")
   print(f" Count Of all Degree: {degree}")







