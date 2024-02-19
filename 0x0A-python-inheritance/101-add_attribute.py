#!/usr/bin/python3

def add_attribute(obj, att, value):
    """Add a new attribute to an object if it's possible.

    Args:
        obj (object): The object to which the attribute should be added.
        attribute_name (str): The name of the new attribute.
        attribute_value: The value of the new attribute.

    Raises:
        TypeError: If the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
