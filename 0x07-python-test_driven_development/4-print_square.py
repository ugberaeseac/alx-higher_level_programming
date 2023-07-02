#!/usr/bin/python3
"""
Module: 4-print_square
prints a square with the character '#'
Takes an int value which is the length of the square
"""


def print_square(size):
    """
    Print the square with '#' using the value of size
    """
    if type(size) not in [int]:
        raise TypeError('size must be an integer')

    elif (size < 0):
        raise ValueError('size must be >= 0')

    elif type(size) in [float] and size < 0:
        raise TypeError('size must be an integer')

    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print()
