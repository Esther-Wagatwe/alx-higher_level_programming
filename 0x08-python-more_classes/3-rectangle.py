#!/usr/bin/python3
"""Defines a rectangle class."""


class Rectangle:
    """Rectangle class with private instance attributes.

    Args:
        width (int): horizontal dimension of rectangle, defaults to 0.
        height (int): vertical dimension of rectangle, defaults to 0.

    Return:
        width and height
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height of the rectangle."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculates and Returns the area of a rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """calculates and Returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((2 * self.__width) + (2 * self.__height))

    def __str__(self):
        """Return the printable representation of a rectangle.
        Rectangle is represented with the # character."""
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectngle = []
        for i in range(self.__height):
            [rectngle.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rectngle.append("\n")
        return ("".join(rectngle))
