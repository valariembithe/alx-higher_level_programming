#!/usr/bin/python3
""" json module """


def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    r = {}
    for key in obj.__dict__:
        value = getattr(obj, key)
        if type(value) in [list, dict, int, bool, str]:
            r[key] = value

    return r
