#!/usr/bin/python3

"""
Module: 100-my_int
Class MyInt that inherits from int
and have operators inverted
"""


class MyInt(int):
    """
    invert operators
    """
    def __init__(self, num):
        """ initialize attribute"""
        self.__num = num

    def __str__(self):
        """
        print representation/description of attribute
        """
        return (str(self.__num))

    def __eq__(self, other):
        """ compare for equality """
        return (self.__num != other)

    def __ne__(self, other):
        """ compare for non-equality """
        return (self.__num == other)
