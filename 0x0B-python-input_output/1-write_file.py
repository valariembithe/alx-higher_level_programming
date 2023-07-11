#!/usr/bin/python3
""" writes file module """


def write_file(filename="", text=""):
    """ writes a string to a text file 
    and returns number of characters """

    string = 0
    with open(filename, "w", encoding="utf-8") as f:
        string = f.write(text)
        
    return string
