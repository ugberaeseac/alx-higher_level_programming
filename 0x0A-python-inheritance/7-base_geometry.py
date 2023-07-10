#!/usr/bin/python3

"""
Module:7-base_geometry
BaseGeometry class that validates an integer value
and raises an exeption
"""


class BaseGeometry:
    """
    raise exception
    """
    def area(self):
        """ raise an exception"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ validates value """
        if type(value) not in [int]:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
