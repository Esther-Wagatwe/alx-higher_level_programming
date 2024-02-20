#!/usr/bin/python3
"""Defines class_to_json"""


def class_to_json(obj):
    """
    function that returns the dictionary description.

    Args:
        obj : is an instance of a Class
        All attributes of the obj Class are serializable
     returns:
        the dictionary description with simple data structure
        for JSON serialization of an object
    """
    return obj.__dict__
