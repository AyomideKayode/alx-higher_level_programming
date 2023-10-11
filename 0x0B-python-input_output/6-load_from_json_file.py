#!/usr/bin/python3

import json

"""
Module to create object from JSON file.
"""


def load_from_json(filename):
    """
    Function to load object from json file.
    Args:
        filename
    Return:
        object created from the file.
    """
    with open(filename, 'r', encoding="UTF8") as obj_file:
        new_file = obj_file.read()
        return json.load(new_file)
