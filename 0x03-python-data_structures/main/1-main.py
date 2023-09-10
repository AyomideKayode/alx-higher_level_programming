#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
# for more test cases
# idx = 4 ...and so on
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))
