#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """method for calculated area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method to validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a Rectangle class that inherits from BaseGeometry.."""
    def __init__(self, width, height):
        """Instantiates a Rectangle with width and height."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
