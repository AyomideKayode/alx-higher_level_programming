#!/usr/bin/python3

# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
old_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
final_list = []  # create an empty list

for i in old_list:  # iterate through each item (tuple) of the list
	temp_list = list(i)  # convert into lists to become mutable
	temp_list[-1] = 100  # replace last idx in lists

	# append new list to result while changing back to tuple
	final_list.append(tuple(temp_list))
print(final_list)

# Write a Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
sample_list = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
filtered_list = []

for x in sample_list:
  if len(x) > 0:
    filtered_list.append(x)

print(filtered_list)

