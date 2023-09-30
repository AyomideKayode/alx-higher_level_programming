#!/usr/bin/python3

"""
Say My Name module
The module takes in input from user of their first name and
last name, then goes on to print `My name is <first name> <last name>`.
Prototype: def say_my_name(first_name, last_name=""):
Raise exceptions is both names aren't string types. Strictly.
"""

def say_my_name(first_name, last_name=""):
    """
    Function that prints user's first name and last name.
    Args:
        User's input of their names.
    Doesn't return shishi
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    else:
        print(f"My name is {first_name} {last_name}")
