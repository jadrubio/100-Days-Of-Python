print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percent = int(input("How much would you like to tip? 10, 12, or 15 percent? "))
num_people = int(input("How many people are splitting the bill? "))

tip = total * (tip_percent * .01)
total_with_tip = total  + tip
per_person_cost = round(total_with_tip / num_people, 2)

print(f"Each person should pay: ${per_person_cost}")