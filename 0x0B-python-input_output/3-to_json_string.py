#!/usr/bin/python3

import json

"""
Module to return json of an object
"""


def to_json_string(my_obj):
    """
    define funcrion to convert an object
    to its JSON representation as a string.

    Args:
        my_obj: The object to be serialized to JSON.
    Returns:
        str: The JSON representation of the object as a string.
    """
    obj_rep = json.dumps(my_obj)
    return obj_rep
