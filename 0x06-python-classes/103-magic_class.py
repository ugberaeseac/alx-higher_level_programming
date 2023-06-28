#!/usr/bin/python3

"""
Define MagicClass to compute area
and circumference
"""
from math import pi


class MagicClass:
    """ defining class MagicClass """
    def __init__(self, radius=0):
        """ Initializing attributes """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ computes the area """
        return ((self.__radius ** 2) * pi)

    def circumference(self):
        """ computes the circumference """
        return (2 * pi * self.__radius)
