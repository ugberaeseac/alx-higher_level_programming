#!/usr/bin/python3

"""
Module: rectangle
Subclass that inherts from superclass Base
"""

from models.base import Base


class Rectangle(Base):
    """
    Class Attributes:
        size

    Inherited Methods:
        Base.init(self, id=None)
        Rectangle.init(self, width, height, x=0, y=0, id=None)
        update(self, *args, **kwargs)
        area(self)       display(self)

    Methods:
        __init(self, width, height, x=0, y=0, id=None)
        __str__(self)
        area(self)
        to_dictionary(self)
        update(self, *args, **kwargs)

    Getters:
        width(self)     x(self)
        height(self)    y (self)

    Setters:
        width(self, value)      x(self, value)
        height(self, value)     y(self, value)
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialize attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        returns an informal string representation of the instance
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width,
            self.height))

    @property
    def width(self):
        """
        Getter:

        Returns:
            width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter:

        Args:
            value: value of width
        """
        if type(value) not in [int]:
            raise TypeError('width must be an integer')

        if value <= 0:
            raise ValueError('width must be > 0')

        self.__width = value

    @property
    def height(self):
        """
        Getter:

        Returns:
            height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter:

        Args:
            value: value of height
        """
        if type(value) not in [int]:
            raise TypeError('height must be an integer')

        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """
        Getter:

        Returns:
            x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter:

        Args:
            value: value of x-axis
        """
        if type(value) not in [int]:
            raise TypeError('x must be an integer')

        if value < 0:
            raise ValueError('x must be >= 0')

        self.__x = value

    @property
    def y(self):
        """
        Getter:

        Returns:
            y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter:

        Args:
            value: value of y axis
        """
        if type(value) not in [int]:
            raise TypeError('y must be an integer')

        if value < 0:
            raise ValueError('y must be >= 0')

        self.__y = value

    def area(self):
        """
        computes the area
        """
        return self.width * self.height

    def display(self):
        """
        Prints Rectangle instance to stdout with the character #
        """
        print("\n" * self.y, end="")
        for rows in range(self.height):
            print(" " * self.x, end="")
            for cols in range(self.width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        assign argument to each attribute
        """
        if (args):
            attribute = [
                    'id', 'width', 'height', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, attribute[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Rectangle instance
        """
        rec_dict = {}

        rec_dict['id'] = self.id
        rec_dict['width'] = self.width
        rec_dict['height'] = self.height
        rec_dict['x'] = self.x
        rec_dict['y'] = self.y

        return (rec_dict)
