import random


choice_img = [
  '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

user_choice = int(input("Press 0 for Rock, 1 for Paper, and 2 for Scissors: "))

cpu_choice = random.randint(0,2)

if user_choice < 0 or user_choice > 2:
  print("You chose....poorly")
  exit(1)

print(f"You chose \n {choice_img[user_choice]}")
print(f"The computer chose \n {choice_img[cpu_choice]}")

if user_choice == cpu_choice:
  print("Tie")
elif (user_choice == 2 and cpu_choice == 0):
  print("You Lose!")
elif (user_choice == 0 and cpu_choice == 2) or (user_choice > cpu_choice):
  print("You Won!")
else:
  print("You Lose!")