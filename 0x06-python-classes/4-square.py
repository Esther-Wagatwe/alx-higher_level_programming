#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new instance of the square class

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """ Get/set the current size of the square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Computes and returns the area of the square
        Returns:
            int: The area of the square
        """
        return (self.__size ** self.__size)
