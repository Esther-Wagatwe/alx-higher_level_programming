#!/usr/bin/python3
"""Defines save_to_json_file method."""
import json as js


def save_to_json_file(my_obj, filename):
    """method that writes an object to a text file using JSON representation.
    Args:
        my_object (object):The Python object to be serialized and saved.
        filename (file): Name of the file to save the JSON representation to.
    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        js.dump(my_obj, file)
