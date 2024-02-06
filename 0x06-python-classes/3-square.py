#!/usr/bin/python3

"""Defining a class square"""


class Square:
    """Representing a class Square."""
    def __init__(self, size=0):
        """Initialize a new square of size new square

        Args:
            size (int): The size of the new square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """computes and returns the area of the square

        Returns:
            int: The area of the square
        """
        return (self.__size * self.__size)
