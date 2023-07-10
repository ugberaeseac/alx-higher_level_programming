#!/usr/bin/python3

"""
Module: 0-lookup
Function that returns a list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    list available attributes and methods
    """
    return (list(dir(obj)))
