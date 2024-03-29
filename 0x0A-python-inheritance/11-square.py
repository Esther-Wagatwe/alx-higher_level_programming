#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class square."""
    def __init__(self, size):
        """Instantiation of a square with size.

        Args:
            size (int): The size of the new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """finding the area."""
        return self.__size ** 2

    def __str__(self):
        """ print and return, the square description."""
        return "[Square] {}/{}".format(self.__size, self.__size)
