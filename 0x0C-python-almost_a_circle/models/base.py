#!/usr/bin/python3

"""
Base class Module inside the Models Python Package.
private class attribute __nb_objects = 0
class constructor: def __init__(self, id=None)::
if id is not None, assign the public instance attribute id
with this argument value - you can assume id is an integer
and you don’t need to test the type of it otherwise,
increment __nb_objects and assign the new value to
the public instance attribute id
Add static method def to_json_string(list_dictionaries):
that returns the JSON string representation of list_dictionaries.
"""

import json


class Base:
    """
    Base class to manage id attribute in all future classes
    and to avoid duplicating the same code
    (by extension, same bugs)
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            # increment __nb_objects & assign the new value to the id attribute
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method to return JSON string representation - list of dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
