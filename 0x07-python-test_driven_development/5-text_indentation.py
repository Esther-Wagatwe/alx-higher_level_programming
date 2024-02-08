#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characs = 0
    while characs < len(text) and text[characs] == ' ':
        characs += 1

    while characs < len(text):
        print(text[characs], end="")
        if text[characs] == "\n" or text[characs] in ".?:":
            if text[characs] in ".?:":
                print("\n")
            characs += 1
            while characs < len(text) and text[characs] == ' ':
                characs += 1
            continue
        characs += 1
