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
            the JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes the JSON string repr of list_objs to a file.
        Args:
            cls (cls): The name of the class
            list_objs (list): list of instances who inherits of Base.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [i.to_dictionary() for i in list_objs]
                jsonfile.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that deserializes json_string.

        Args:
            json_string (str): string representing a list of dictionaries.
        Return:
            the list represented by json_string.
        """
        if json_string is None or not json_string:
            return []
        else:
            return json.loads(json_string)
