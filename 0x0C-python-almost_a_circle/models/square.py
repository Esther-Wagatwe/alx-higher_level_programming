#!/usr/bin/python3
"""Defines class Square that inherits from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square. Square is a special rectangle."""
    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor, initialize instance attributes."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a Square.

        Returns:
            str: Info about the square
            """
        return "[{}] ({}) {}/{} - {}".\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Get/ set the value of size."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value
