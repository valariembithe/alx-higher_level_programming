#!/usr/bin/python3
"""Contains a class that inherits from `BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ a class Rectangle """
    def __init__(self, width, height):
        """ Initializes width and height """
        self.integer_validator = ("width", width)
        self.__width = width
        self.integer_validator = ("height", height)
        self.__height = height

    def area(self):
        """ gets area of rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ prints rectangle description """
        string = ("[Rectangle] {}/{}".format(self.__width, self.__height))
        return string
