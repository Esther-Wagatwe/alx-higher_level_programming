#!/usr/bin/python3
"""Defines a function is_same_class."""


def is_same_class(obj, a_class):
    """Method that return True if an object is an instance of a class
    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
