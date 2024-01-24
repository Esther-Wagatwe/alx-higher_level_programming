#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = []
    for row in matrix:
        squared_row = list(map(lambda x: x**2, row))
        matrix_squared.append(squared_row)
    return (matrix_squared)
