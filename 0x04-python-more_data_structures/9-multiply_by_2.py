#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    list_key = list(new.keys())

    for i in list_key:
        new[i] *= 2
    return (new)
