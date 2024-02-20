#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    pas = []
    if n <= 0:
        return pas

    for row in range(n):
        for colmn in range(row + 1):
            if colmn == 0:
                pas.append([1])
            elif colmn == row:
                pas[row].append(1)
            else:
                pas[row].append(pas[row - 1][colmn] + pas[row - 1][colmn - 1])
    return pas
