#!/usr/bin/python3

"""
Module: 8-base_geometry
Rectangle class that inherits from BaseGeometry class
and validates an integer value for height and width
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    integer validation of width and height
    and initializaion of attributes
    """
    def __init__(self, width, height):
        """
        validate and initialize
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
