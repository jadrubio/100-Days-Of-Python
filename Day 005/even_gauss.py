target = int(input("Please enter the ending number we are going to be adding until: "))
total = 0

for number in range(2,target + 1, 2):
  total += number

print(f"the numbers of 0 to 100 added together = {total}")