#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry.."""
    def __init__(self, width, height):
        """Instantiates a Rectangle with width and height.
        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method to redefine a area method in the parent class"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
