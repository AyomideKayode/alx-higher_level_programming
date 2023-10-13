#!/usr/bin/python3

"""
Square Class Module that inherits from Rectangle:
Inits superclass' id, width (as size), height (as size), x, y
Class constructor: __init__(self, size, x=0, y=0, id=None)
Contains public attribute size
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Defines Square class that inherits from Rectangle.
    Inherited attributes of:
        id (Base), __width, __height, __x & __y
    Inherited methods of:
        Base.init(self, id=None);
        Rectangle.init(self, width, height, x=0, y=0, id=None);
        update(self, *args, **kwargs); width(self), width(self, value);
        height(self), height(self, value); x(self), x(self, value);
        y(self), y(self, value); area(self); display(self);
    Class Attribute:
        size
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.
        Args:
            size (int): Size of the square.
            x (int, optional): X coordinate. Defaults to 0.
            y (int, optional): Y coordinate. Defaults to 0.
            id (int, optional): ID of the square. Defaults to None.
        """
        # call superclass constructor with all parameters
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Print out string representation of the Square instance.
        Returns:
            str: A string in the format [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width))
