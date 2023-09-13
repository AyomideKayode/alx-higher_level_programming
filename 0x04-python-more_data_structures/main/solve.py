#!/usr/bin/python3

# Write a Python program to replace the last value of tuples in a list.
# Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

new_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
print(new_list)
# convert list items to list elements
list1 = list(new_list[0])
list2 = list(new_list[1])
list3 = list(new_list[2])
# print individual lists out
print(list1)
print(list2)
print(list3)
# change last items
list1[2] = 100
list2[2] = 100
list3[2] = 100
# combine them back
all_list = list1 + list2 + list3
print(all_list)
# make them back into tuples
tuple1 = tuple(list1)
tuple2 = tuple(list2)
tuple3 = tuple(list3)
list_new = [tuple1, tuple2, tuple3]
print(list_new)
