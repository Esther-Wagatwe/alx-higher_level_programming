#!/usr/bin/python3
"""Defining a function read_file."""


def read_file(filename=""):
    """read_file function reads a text file and prints it stdout."""
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read(), end="")
