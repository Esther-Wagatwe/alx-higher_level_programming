#!/usr/bin/python3
"""Defines a method load_from_json_file."""
import json as js


def load_from_json_file(filename):
    """
    Create an object from a JSON file
    Args:
        filename (file): Name of the file containing the JSON representation.
    Returns:
        object: The Python object represented by the JSON file.
    """
    with open(filename, "r") as file:
        return js.load(file)
