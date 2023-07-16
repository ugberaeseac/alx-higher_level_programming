#!/usr/bin/python3

"""

"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        returns an informal string representation of the instance
        """
        return ("[{:s}] ({:d}) {:d}/{:d} - {:d}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """
        Getter:

        Returns:
            size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter

        Args:
            value: value of height and weight
        """
        self.width = value
        self.height = value
