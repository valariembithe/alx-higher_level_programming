#!/usr/bin/python3
""" checks for lowercase character."""
def islower(c):
    if ord(c) >= 97 or ord(c) <= 122:
        return True
    else:
        return False
