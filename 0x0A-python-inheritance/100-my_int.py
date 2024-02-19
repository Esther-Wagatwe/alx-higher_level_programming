#!/usr/bin/python3
"""Defines MyInt class."""


class MyInt(int):
    """MyInt class inherits from int."""
    def __eq__(self, value):
        """Override == operator with != operator."""
        return super().__ne__(value)

    def __ne__(self, value):
        """Override != operator with == operator."""
        return super().__eq__(value)
