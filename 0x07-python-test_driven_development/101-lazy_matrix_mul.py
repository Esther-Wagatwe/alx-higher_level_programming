#!/usr/bin/python3
import numpy as np
"""Defining a lazy matrix multiplication."""


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: Resulting matrix.

    Raises:
        ValueError: If matrices cannot be multiplied.
    """
    return (np.matmul(m_a, m_b))
