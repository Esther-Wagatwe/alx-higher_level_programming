#!/usr/bin/python3
"""Define a class MyList that inherits from list."""


class MyList(list):
    """Implements sorted printing for the built-in list class."""
    def print_sorted(self):
        """a method that prints the list, but sorted (ascending sort)."""
        print(sorted(self))
