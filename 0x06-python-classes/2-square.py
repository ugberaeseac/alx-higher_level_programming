#!/usr/bin/python3
"""
Module 1-square
A class Square that defines a square by
private instance attribute
"""


class Square:
    """
    defines a class square

    Attributes:
        size: size of the square
    """
    def __init__(self, size=0):
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
