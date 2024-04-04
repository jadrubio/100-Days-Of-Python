import random

names_string = input("Please list out the names of everyone at the table (comma separated)")
names = names_string.split(", ")

num_names = len(names)
rand_index = random.randint(0, num_names-1)
bill_payer = names[rand_index]

print(f"I have choosen {bill_payer} to pick up the tab!")