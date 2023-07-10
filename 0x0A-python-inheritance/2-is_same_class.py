#!/usr/bin/python3

"""
Module: 2-is_same_class
Function that returns True if object is an instance
of specified class, else returns False
"""


def is_same_class(obj, a_class):
    """
    check if object is instance of specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
