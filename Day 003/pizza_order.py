print("Welcome to Pizza Py(thon)!")
price = 0


size = input("What size pizza do you want? s/m/l ").lower()
if size == 's':
  price = 15
elif size == 'm':
  price = 20
elif size == 'l':
  price = 25
else:
  print(f"We do not make pizzes in size {size}")
  exit(1)

add_pepperoni = input("Would you like to add pepperoni? y/n ").lower()
if add_pepperoni == 'y':
  if size == 's':
    price += 2
  else:
    price += 3

extra_cheese = input("Would you like extra cheese? y/n ").lower()
if extra_cheese == 'y':
  price += 1

print(f"Your final bill comes out to ${price}")