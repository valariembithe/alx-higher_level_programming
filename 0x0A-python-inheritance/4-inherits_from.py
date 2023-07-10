#!/usr/bin/python3
""" Module """


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class that inherited
    """
    return ((issubclass(type(obj), a_class)) and type(obj) != a_class)
