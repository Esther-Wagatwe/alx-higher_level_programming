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
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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

        rect = []
        for i in range(self.__height):
            [rect.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the rectangle.
        Allow use of eval"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """Prints message once an instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method that returns the biggest rectangle baser on the area.
        Args:
            rect_1 (Rectangle object): first instance to be compared
            rect_2 (Rectangle object): second instance to be compared

        Raises:
            TypeError: if `rect_1` or `rect_2` is not an instance of cls.

        Returns:
            `rect_1` if `rect_1` has an area larger than or equal to `rect_2`,
        or `rect_2` if it has the larger area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns an instance with equal size of length and width.

        Args:
            size (int): length of sides of square, defaults to 0.

        Returns:
            new instance of class with equal sides

        """
        return cls(size, size)
