target = int(input("Please enter the ending number we are going to be counting until: "))

for n in range(0, target + 1):
  if(n % 15 == 0):
    print("FizzBuzz")
  elif(n % 5 == 0):
    print("Buzz")
  elif(n % 3 == 0):
    print("Fizz")
  else:
    print(n)