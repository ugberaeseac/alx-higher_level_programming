#!/usr/bin/python3

"""
Module: 101-add_attribute
A function that adds a new attribute to an object
if it’s possible
"""


def add_attribute(objt, attrib, value):
    """
    add attribute if possible
    """
    if hasattr(objt, '__dict__'):
        setattr(objt, attrib, value)
    else:
        raise TypeError("can't add new attribute")
