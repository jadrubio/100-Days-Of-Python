print("Welcome to the BMI calculator - keep in mind this is a poor marker for health")
height = input("What is your height in meters?\n")
weight = input("What is your weight in kilos?\n")

bmi = float(weight)/float(height) ** 2
print("Your BMI is ", int(bmi))

if bmi < 18.5:
  print("You are underweight")
elif bmi < 25:
  print("You are at a normal weight")
elif bmi < 30:
  print("You are slightly overweight")
elif bmi < 35:
  print("You are obese")
elif bmi > 35:
  print("You are clinically obese")
