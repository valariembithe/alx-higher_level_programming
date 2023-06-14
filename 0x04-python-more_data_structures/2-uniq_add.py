#!/usr/bin/python33
def uniq_add(my_list=[]):
    num = 0
    new_list = set(my_list)
    for i in new_list:
        num += i

    return (num)
