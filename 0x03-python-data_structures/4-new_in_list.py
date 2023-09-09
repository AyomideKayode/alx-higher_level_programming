#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    cp_list = my_list.copy()
    num_element = len(my_list)
    if idx < 0:
        return cp_list
    if idx >= num_element:
        return cp_list

    cp_list[idx] = element
    return cp_list
