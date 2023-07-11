#!/usr/bin/python3

"""
Module: 10-square
class Square inherits from class Rectangle validates value
and implement the area of the square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    validates values and computes the area
    """
    def __init__(self, size):
        """
        initialize attributes
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ computes the area """
        return (self.__size * self.__size)
