#!/usr/bin/python3
"""Defines add_attribute Module"""


def add_attribute(obj, attribute, att_value):
    """Adds a new attribute to the object"""
    if not hasattr(obj, "__slots__") and not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    if hasattr(obj, "__slots__") and not hasattr(obj, attribute):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, att_value)
