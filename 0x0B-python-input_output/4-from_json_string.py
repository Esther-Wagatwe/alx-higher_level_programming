#!/usr/bin/python3
"""Defines a function from_json_string."""
import json


def from_json_string(my_str):
    """Function deserialzes JSON object.
    Args:
        my_str (): A JSON-formatted string
    Returns:
        an object (Python data structure) representation of  a JSON string
    """
    return json.loads(my_str)
