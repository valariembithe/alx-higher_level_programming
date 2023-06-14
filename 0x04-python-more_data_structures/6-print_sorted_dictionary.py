#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    list_key = list(a_dictionary.keys())
    list_key.sort()
    for i in list_key:
        print("{} : {}".format(i, a_dictionary.get(i)))

