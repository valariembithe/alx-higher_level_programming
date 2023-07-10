#!/usr/bin/python3
""" Module of MyList """


class MyList(list):
    """ prints the list, but sorted (ascending sort) """
    def print_sorted(self):
        print(sorted(self))
