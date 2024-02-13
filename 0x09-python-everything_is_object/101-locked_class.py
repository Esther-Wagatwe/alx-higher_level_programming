#!/usr/bin/python3
"""Define class LockedClass with no class or object attribute, that prevents
the user from dynamically creating new instance attribute"""


class LockedClass:
    """
    Define LockedClass

    Attributes:
        first_name (str): first name of something.
    """
    __slots__ = ["first_name"]

    def __init__(self):
        """Creates new instances of Locked Class."""
        self.first_name = "first_name"
