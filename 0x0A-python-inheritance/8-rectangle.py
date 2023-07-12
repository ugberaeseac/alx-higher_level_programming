#!/usr/bin/python3

"""
Module: 8-base_geometry
Rectangle class that inherits from BaseGeometry class
and validates an integer value for height and width
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


class Rectangle(BaseGeometry):
    """
    integer validation of width and height
    and initializaion of attributes
    """
    def __init__(self, width, height):
        """
        validate and initialize
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
