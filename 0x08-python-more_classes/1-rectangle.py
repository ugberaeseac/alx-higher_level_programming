#!/usr/bin/python3

"""
Module: 1-rectangle
a class Rectangle that defines a rectangle
raises exception if width and height is not int
"""


class Rectangle:
    """
    defines a rectangle

    Args:
        width(int): width
        height(int): height

    Functions:
        __init__(self, width, height)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
    """
    def __init__(self, width=0, height=0):
        """
        initialize attributes
        """
        self.width = width
        self.height = height

    @property
    def height(self):
        """
        Getter

        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter

        Args:
            value: value of height passed as parameter
        """
        if type(value) not in [int]:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    @property
    def width(self):
        """
        Getter

        Returns:
            width
        """
        return self.__width

    @height.setter
    def width(self, value):
        """
        Setter

        Args:
            value: value of width passed as parameter
        """
        if type(value) not in [int]:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value
