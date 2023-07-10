#!/usr/bin/python3
""" Module MyInt """


class MyInt(int):
    """ inherits from int """
    def __init__(self,value):
        """ initialize value """
        self.value = value

    def __ne__(self, x):
        """ not equal """
        if self.value is x:
            return True

    def __eq__(self, x):
        """ equal """
        return not self.__ne__(x)
