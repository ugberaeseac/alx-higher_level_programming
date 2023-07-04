#!/usr/bin/python3
"""
Module: 101-locked_class
class with no class or object attribute
that prevents the user from dynamically creating new instance attributes
"""


class LockedClass():
    """
    prevent dynamically created instances 
    except instance attribute is 'first_name'
    """

    __slots__ = "first_name"
