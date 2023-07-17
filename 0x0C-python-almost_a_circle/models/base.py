#!/usr/bin/python3
""" Class module named Base base.py"""
import json
import csv
import os
import turtle


class Base:
    """ private instance nb objects """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialize class objects """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
