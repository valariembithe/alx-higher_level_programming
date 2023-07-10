#!/usr/bin/python3
""" single funvtion """


def add_attribute(self, attribute, value):
    """ ADD attribute if possible """
    if hasattr(self, '__dict__'):
        setattr(self, attribute, value)
    else:
        raise TypeError("can't add new attribute")
