#!/usr/bin/python3

"""
Create class Rectangle that defines a rectangle by
private instance attribute: width:, and
private instance attribute: height:
Methods getter and Setter properties for the width and height
And raising errors if certain conditionas are not met.
"""


class Rectangle:
    """
    Instantiating variables of width and height

    Args:
        width (int)
        height (int)
    Dazzit, Dazzall.
    """
    def __init__(self, width=0, height=0):
        # initialize private attributes
        self.__width = width
        self.__height = height

    @property
    def width(self):
        # property to retrive width
        return self.__width

    @width.setter  # setter method for width
    def width(self, value):
        # verify that value is an integer
        if type(value) is not int:
            raise TypeError("width must be an integer")

        # check that value is >= 0
        if value < 0:
            raise ValueError("width must be >= 0")

        # update private instance attribute
        self.__width = value

    @property
    def height(self):
        # property to retrive height
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        # verify that value is an integer
        if type(value) is not int:
            raise TypeError("height must be an integer")

        # check that value is >= 0
        if value < 0:
            raise ValueError("height must be >= 0")

        # update private instance attribute
        self.__height = value
