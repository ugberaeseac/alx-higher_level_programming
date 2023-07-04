#!/usr/bin/python3

"""
Module: 101-locked_class
class with no object attribute that prevents user
from dynamically creating new instance attributes except first_name
"""

class LockedClass:
    """
    prevent dynamically created instances
    except 'first_name'
    """

    __slots__ = "first_name"
