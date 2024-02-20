#!/usr/bin/python3
"""Defining append_write method."""


def append_write(filename="", text=""):
    """Defines a method that appends a string at the end of a text file.
    Args:
        filename (str): The name of the file to append to
        text (str): The text to append
    Return:
        number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
