print("Welcome fot he rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  age = int(input("How old are you? "))
  if age <= 18:
    print("A ticket cost $7")
  else:
    print("A ticket cost $12")
else:
  print("Eat more veggies and grow taller to ride")