#!/usr/bin/python3
"""Defines write_file function."""


def write_file(filename="", text=""):
    """method that writes a string to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
