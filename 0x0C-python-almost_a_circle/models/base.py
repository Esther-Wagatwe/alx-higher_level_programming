#!/usr/bin/python3
"""Defines a class that will be the base of all other classes."""
import json
import csv


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
            cls (class): The name of the class
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

    @classmethod
    def create(cls, **dictionary):
        """
        Args:
            cls (class): The name of the class.
            dictionary (dict): a double pointer to a dictionary.

        returns:
            an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)

        if cls.__name__ == "Square":
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Class method that loads string from file and deserializes it.

        returns:
            a list of instances:
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [cls.create(**i)
                        for i in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        serializes in CSV.
        """
        filename = cls.__name__ + ".json"
        content = []
        for i in range(len(list_objs)):
            content.append(cls.to_dictionary(list_objs[i]))
        with open(filename, 'w') as f:
            if cls.__name__ == "Rectangle":
                columns = ['id', 'width', 'height', 'x', 'y']
            if cls.__name__ == "Square":
                columns = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(f, fieldnames=columns)
            writer.writeheader()
            writer.writerows(content)

    @classmethod
    def load_from_file_csv(cls):
        """
        Deserialise in csv.
        """
        filename = cls.__name__ + ".json"
        mylist = []
        try:
            with open(filename, "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    mylist.append(row)
                instances_list = []
                for i in range(len(mylist)):
                    instances_list.append(cls.create(**mylist[i]))
        except:
            instances_list = []

        return instances_list
