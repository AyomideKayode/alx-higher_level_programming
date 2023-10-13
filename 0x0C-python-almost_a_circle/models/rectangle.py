#!/usr/bin/python3

"""
Rectangle Class Module that inherits from Base:
Private instance attributes, each with its own public getter and setter:
__width -> width, __height -> height
__x -> x, __y -> y
Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
Call the super class with id -
this super call will use the logic of the __init__ of the Base class
Assign each argument width, height, x and y to the right attribute
Update with public methods of area and display:
def area(self): that returns the area value of the Rectangle instance
def display(self): prints in stdout the Rectangle instance with the character #
"""


from models.base import Base


class Rectangle(Base):
    """
    Defines Rectangle class that inherits from base.
    Inherited attribute of: id
    Class attributes of:
        __width, __height, __x & __y
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)  # call superclass constructor with id parameter
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # Set public getters and setters for each attribute
    # Width
    @property
    def width(self):
        """ Getter for width.
        Return: width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError('{} must be an integer'.format('width'))
        if value <= 0:
            raise ValueError("width must be > 0")
        # update private instance atrribute
        self.__width = value

    # Height
    @property
    def height(self):
        """Getter for height.
        Return: height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        # update private instance attribute
        self.__height = value

    # X
    @property
    def x(self):
        """Getter for X
        Return: x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter fo x.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        # update private instance attribute
        self.__x = value

    # Y
    @property
    def y(self):
        """Getter for Y
        Return: y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y.
        Raise exceptions where necessary."""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        # update private instance attribute
        self.__y = value

    # Public Methods:
    # Area
    def area(self):
        """Calculate and returns the area of the Rectangle instance.
        """
        return (self.__width * self.__height)

    # Display
    def display(self):
        """Function that display(print) to stdout
        the Rectangle instance with the `#` character."""
        for i in range(self.__height):
            print("#" * self.__width)
