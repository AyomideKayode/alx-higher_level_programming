#!/usr/bin/python3

import json

"""
Module to create object from JSON file.
"""


def load_from_json_file(filename):
    """
    Function to load object from json file.
    Args:
        filename
    Return:
        object created from the file.
    """
    with open(filename) as obj_file:
        new_file = json.load(obj_file)
        return new_file
