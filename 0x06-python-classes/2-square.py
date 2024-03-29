#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square."""
    def __init__(self, size=0):
        """ Initialize a square instance.


        Args:
            size(int): The size of the square(default is 0)


        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
