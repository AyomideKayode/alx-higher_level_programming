#!/usr/bin/python3

squares = [] #  creating a list with results of sequences.
for x in range(10):
	squares.append(x**2)

print(squares)

cubes = []
for c in range(3, 15):
	cubes.append(c**3)

print(cubes)


#  instaed of the loop, another way might be to:
new_squares = [x**2 for x in range(15)]
print(f"New square style is: {new_squares}")