#!/usr/bin/python3
class LockedClass:
    """
    prevent dynamically created instances except 'first_name'
    """
    __slots__ = ["first_name"]
