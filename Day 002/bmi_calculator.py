height = input("What is your height in meters?\n")
weight = input("What is your weight in kilos?\n")

bmi = float(weight)/float(height) ** 2
print("Your BMI is ", int(bmi))