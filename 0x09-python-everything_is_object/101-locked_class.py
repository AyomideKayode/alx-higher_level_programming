#!/usr/bin/python3


class LockedClass:
    """
    Class that prevents the user from dynamically creating any new
    instance attributes, except if new attribute is called `first_name`
    """
    __slots__ = ['first_name']
