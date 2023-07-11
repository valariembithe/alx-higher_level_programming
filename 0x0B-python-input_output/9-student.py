#!/usr/bin/python3
""" class module"""


class Student:
    """ class named student"""
    def __init__(self, first_name, last_name, age):
        """ initialize student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation"""
        r = {}
        for key in self.__dict__:
            value = getattr(self, key)
            if type(value) in [list, dict, str, int, bool]:
                r[key] = value
        return r
