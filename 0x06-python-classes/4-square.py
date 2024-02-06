#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""
    def __init__(self, size=0):
        """
        Initialize a new instance of the square class

        Args:
            size (int): The size of the square
        """

        self.__size = size

    @property
    def size(self):
        """ get the current size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (int): The size to set

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and returns the area of the square"""
        return self.__size ** 2
