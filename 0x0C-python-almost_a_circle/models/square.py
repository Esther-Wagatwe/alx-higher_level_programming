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

    def update(self, *args, **kwargs):
        """Method to assign attributes."""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    self.x = args[i]
                elif i == 3:
                    self.y = args[i]

        elif kwargs is not None and len(kwargs) != 0:
            for key in (kwargs):
                if key == "id":
                    self.id = kwargs[key]
                elif key == "size":
                    self.width = kwargs[key]
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
        create dictionary representation of a square.

        Return:
            the dictionary representation of a square.
        """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
