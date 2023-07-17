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

    def update(self, *args, **kwargs):
        """
        assign argument to each attribute
        """
        if (args):
            attribute = [
                    'id', 'size', 'x', 'y']
            for index, value in enumerate(args):
                setattr(self, attribute[index], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of a Square instance
        """
        sqr_dict = {}

        sqr_dict['id'] = self.id
        sqr_dict['size'] = self.size
        sqr_dict['x'] = self.x
        sqr_dict['y'] = self.y

        return (sqr_dict)
