#!/usr/bin/python3
cubes = [1, 8, 27, 65, 81, 125]  # wring value of cube 4
print(cubes)
cubes[3] = 64  # replace index value
print(cubes)
cubes.append(216)  # append item to list
cubes.append(7 ** 3)
print(cubes)

# Remove and append with slicing method and also use len()
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']  # replace some values
print(letters)
letters[2:5] = []  # remove them totally
print(letters)
print(len(letters))  # use builtin to know length of current list

# use nesting
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)  # print the nested list
# also get specific list in the nest or index of list1/2
print(x[0])
print(x[0][2])
