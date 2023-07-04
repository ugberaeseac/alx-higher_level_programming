#!/usr/bin/python3

"""
Module: 1-rectangle
a class Rectangle that defines a rectangle
raises exception if width and height is not int
"""


class Rectangle:
    """
    defines a rectangle

    Attributes:
        number_of_instances(int): number of objects(instances)

    Args:
        width(int): width
        height(int): height

    Functions:
        __init__(self, width, height)
        height(self)
        height(self, value)
        width(self)
        width(self, value)
        area(self)
        perimeter(self)
        __str__(self)
        __repr__(self)
        __del__(self)
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        initialize attributes
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        returns an informal string representation of the rectangle
        """
        rectangle = ""
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height - 1):
            rectangle += str(self.print_symbol) * self.width + "\n"
        rectangle += str(self.print_symbol) * self.width
        return rectangle

    def __repr__(self):
        """
        returns the fficial string representation of the rectangle
        """
        return ("Rectangle({:d}, {:d})".format(self.width, self.height))

    def __del__(self):
        """
        print a message when a rectangle is deleted
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

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

    @width.setter
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

    def perimeter(self):
        """
        Returns:
            perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def area(self):
        """
        Returns:
            area of the rectangle
        """
        return (self.__height * self.__width)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compare two rectangles
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')

        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns:
            a new Rectangle instance
        """
        return cls(size, size)
