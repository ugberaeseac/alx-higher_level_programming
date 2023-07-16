#!/usr/bin/python3

"""

"""

from models.base import Base


class Rectangle(Base):
    """
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
        for rows in range(self.height):
            for cols in range(self.width):
                print("#", end="")
            print()
