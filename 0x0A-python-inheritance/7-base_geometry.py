#!/usr/bin/python3
"""Defines a BaseGeometry class."""


class BaseGeometry:
    """"Defines an empty class BaseGeometry."""
    def area(self):
        """method that raises an Exception.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """method that validates value."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
