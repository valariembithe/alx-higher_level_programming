#!/usr/bin/python3
"""
    a class defined Rectangle
    string __str__ representation
"""


class Rectangle:
    """ a class that defines Rectangle
        Args: width of type int
              height of type int
    """
    def __init__(self, width=0, height=0):
        """ instances for width and height """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ set the width to retrive it """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ properties of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ set the height to retrive it """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ properties of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ return area of rectangle """
        return (self.__width * self.__height)

    def perimeter(self):
        """ return perimeter of a rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """ returns a rectangle with # """
        if self.__width == 0 or self.__height == 0:
            return ""
        pic = "\n".join(["#" * self.__width for rows in range(self.__height)])
        return pic
