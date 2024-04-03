print("Welcome fot he rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  age = int(input("How old are you? "))
  if age < 12:
    print("A ticket cost $5")
    bill = 5
  elif age <=18:
    print("A ticket cost $7")
    bill = 7
  else:
    print("A ticket cost $12")
    bill = 12

  wantsPhoto = input("Would you like a photo? y/n ")
  if wantsPhoto == 'y':
    bill += 3

  print(f"Your total bill is ${int(bill)}")
else:
  print("Eat more veggies and grow taller to ride")