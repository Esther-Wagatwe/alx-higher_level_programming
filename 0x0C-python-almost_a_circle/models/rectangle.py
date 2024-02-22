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

    def area(self):
        """
        Method that calculates the area of a rectangle.

        returns: the area.
        """
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle instance with the character #."""
        s = '\n' * self.y + \
            (' ' * self.x + '#' * self.width + '\n') * self.height
        print(s, end='')

    def __str__(self):
        """Returns string info about this rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns arguments to attributes: id, width, height, x, y."""
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.__width = args[i]
                elif i == 2:
                    self.__height = args[i]
                elif i == 3:
                    self.__x = args[i]
                elif i == 4:
                    self.__y = args[i]
        elif kwargs is not None and len(kwargs) != 0:
            for key in kwargs:
                if key == "id":
                    self.id = kwargs[key]
                elif key == "width":
                    self.width = kwargs[key]
                elif key == "height":
                    self.height = kwargs[key]
                elif key == "x":
                    self.x = kwargs[key]
                elif key == "y":
                    self.y = kwargs[key]

    def to_dictionary(self):
        """
        create dictionary representation of a rectangle.

        Returns:
            dictionary representation of a rectangle.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
            }
