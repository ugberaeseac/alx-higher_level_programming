#!/usr/bin/python3

"""
Module: 4-inherits_from
Function that returns True if object is an instance of a class that
inherited directly or indirectly from a specified class, else returns False
"""


def inherits_from(obj, a_class):
    """
    check if object is instance of class that inherited
    directly or indirectly from a specific class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
