def calculate_true(name):
  score = 0
  for letter in name:
    match letter.lower():
      case 't':
        score += 1
      case 'r':
        score += 1
      case 'u':
        score += 1
      case 'e':
        score += 1
  return score

def calculate_love(name):
  score = 0
  for letter in name:
    match letter.lower():
      case 'l':
        score += 1
      case 'o':
        score += 1
      case 'v':
        score += 1
      case 'e':
        score += 1
  return score

print("Love Calculator")
userName = input("What is your name? ")
crushName = input("What is your crushes name? ")

true_score = calculate_true(userName)
true_score += calculate_true(crushName)

love_score = calculate_love(userName)
love_score += calculate_love(crushName)

print(f"Your love scores is : {true_score}{love_score}")