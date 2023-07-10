#!/usr/bin/python3

"""
Module: 2-is_kind_of_class
Function that returns True if object is an instance of a class
that inherited from a specified class, else returns False
"""


def is_kind_of_class(obj, a_class):
    """
    check if object is instance of class
    or inherited from a specific class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
