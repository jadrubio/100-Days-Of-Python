line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]
map = [line1, line2, line3]

print("Hiding your treasure! X marks the spot.")
position = input("Give the coordinates for where you are hiding your treasure: ")


xcoord = ["a", "b", "c"].index(position[0].lower())

ycoord = int(position[1])-1

map[ycoord][xcoord] = 'X'

print(f"{line1}\n{line2}\n{line3}")