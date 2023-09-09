#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:  # check if list is empty
        return None
    max_int = my_list[0]  # initially set 1st idx as max int
    for i in my_list[1:]:  # starting from 2nd idx since 1st has been initialised
        if i > max_int:
            max_int = i
    return max_int
