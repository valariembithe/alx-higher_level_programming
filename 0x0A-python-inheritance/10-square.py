#!/usr/bin/python3
""" Module Square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class named Square """
    def __init__(self, size):
        """ Initialize size"""
        self.integer_validator = ("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
