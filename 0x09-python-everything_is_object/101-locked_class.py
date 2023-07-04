#!/usr/bin/python3
class LockedClass:
    """prevent dynamically created instances except attribute 'first_name'
    """
    __slots__ = ['first_name']
