#!/usr/bin/python3
"""Defines a class Rectangle that inherits from base."""
from models.base import Base


class Rectangle(Base):
    """Class that forms a rectangle."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class representing a rectangle

        Attributes:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle's position.
            y (int): The y-coordinate of the rectangle's position.
            id (int): The identifier of the rectangle.

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
        def width(self, x):
            """Set the width of the rectangle."""
            self.__width = self.__x

        @property
        def height(self):
            """Set the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, y):
            """Get the height of the rectangle."""
            self.__height = self.__y
