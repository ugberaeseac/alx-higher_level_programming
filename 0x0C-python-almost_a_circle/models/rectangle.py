#!/usr/bin/python3

"""

"""

from models.base import Base


class Rectangle(Base):
    """
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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
        pass

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
        pass

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
        pass

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
        pass
