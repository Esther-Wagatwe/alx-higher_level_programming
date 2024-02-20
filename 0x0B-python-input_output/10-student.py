#!/usr/bin/python3
"""Defines class_to_json"""


class Student:
    """ Class that defines a student."""
    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        function that returns the dictionary description.
        Returns:
            the dictionary description with simple data structure
            for JSON serialization of an object
        """
        if (type(attrs) == list and all(type(elem) == str for elem in attrs)):
            result = {}
            for i in attrs:
                if hasattr(self, i):
                    result[i] = getattr(self, i)
            return result
        return self.__dict__
