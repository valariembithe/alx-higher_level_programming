#!/usr/bin/python3

def add_integer(a, b=98):
    """
        adds two integers
        Args: a: an integer or float
              b: an integer or float

        Return:sum of a and b
    """
    if type(a) is not int:
        a = int(a)
    if type(b) is not int:
        b = int(b)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is not int:
        raise TypeError("b must be an integer")

    return (a + b)
