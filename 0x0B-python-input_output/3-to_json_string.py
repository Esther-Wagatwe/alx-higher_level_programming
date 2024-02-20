#!/usr/bin/python3
"""Defines to_json_string method."""
import json as js


def to_json_string(my_obj):
    """Method that convert a Python object to a JSON-formatted string.
    Args:
        my_obj (object): Any Python object that is serializable to JSON.
    Returns:
        the JSON representation of the object (string).
    """
    return js.dumps(my_obj)
