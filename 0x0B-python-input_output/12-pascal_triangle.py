#!/usr/bin/python3
""" pascal triangle module """


def pascal_triangle(n):
    """ returns a list of lists of integers representing the Pascal’s """
    pascal = []
    curr = []
    prev = []

    while n > 0:
        prev = curr
        curr = curr + [1]
        i = 1
        while i < len(prev):
            curr[i] = prev[i - 1] + prev[i]
            i += 1
        pascal.append(curr)
        n -= 1

    return pascal
