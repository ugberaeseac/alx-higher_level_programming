#!/usr/bin/python3

"""
Module: 9-rectangle
A class Rectangle that inherits from BaseGeometry class
validates values, computes area and prints magic word
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

    def __str__(self):
        """
        Return rectangle description : [Rectangle] <width>/<height>
        """
        return ("[{:s}] {:d}/{:d}".format(self.__class__.__name__,
                                          self.__width, self.__height))

    def area(self):
        """
        compute the area of the rectangle
        """
        return (self.__width * self.__height)
