#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_copy = a_dictionary.copy()
    list_key = list(dict_copy.keys())
    list_key.sort()
    for i in list_key:
        print("{}: {}".format(i, dict_copy.get(i)))
