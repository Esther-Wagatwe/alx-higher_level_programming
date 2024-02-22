#!/usr/bin/python3
"""Defines a class that will be the base of all other classes."""


class Base:
    """Class to manage id attribute in all future classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
