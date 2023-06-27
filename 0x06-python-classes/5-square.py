#!/usr/bin/python3
"""
Module 1-square
A class Square that defines a square by
private instance attribute
"""


class Square:
    """
    defines a class square

    Attributes:
        size: size of the square
    """
    def __init__(self, size=0):
        """
        Initialize object
        """
        self.__size = size

    def area(self):
        """
        Calculates the area of the square


        Returns:
            The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Getter

        Returns:
            size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: Value passed as parameter

        Returns: value if size = type int and  >= 0
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """
        prints in stdout the square with the character #
        """
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
