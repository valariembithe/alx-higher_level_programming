#!/usr/bin/python3
"""
    contains class rectangle
    with private instances
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
