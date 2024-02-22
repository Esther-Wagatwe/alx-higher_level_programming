#!/usr/bin/python3
"""Defines a class that will be the base of all other classes."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Serializes list_dictionaries.

        Args:
            list_dictionaries (object): a list of dictionaries.

        returns:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
