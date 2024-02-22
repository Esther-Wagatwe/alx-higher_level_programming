#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """Class that forms a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class representing a rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        self.validate_int("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Get the height of the rectangle."""
        self.validate_int("height", value, False)
        self.__height = value

    @property
    def x(self):
        """Get/set x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_int("x", value)
        self.__x = value

    @property
    def y(self):
        """Get/set y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_int("y", value)
        self.__y = value

    def validate_int(self, attribute, value, eq=True):
        """Method to validate all setter methods and instantiation."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(attribute))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(attribute))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(attribute))
