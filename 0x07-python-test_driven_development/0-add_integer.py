#!/usr/bin/python3
"""
Module: 0-add_integer
Takes two arguments, casts them to integers and computes the sum
Returns an integer: the sum of 'a' and 'b'
"""


def add_integer(a, b=98):
    """
    Adds two integers and return an int
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    elif type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    else:
        return (int(a) + int(b))
