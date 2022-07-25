#!/usr/bin/python3
"""Module lazy_matrix_mul
Matrix multiplication using NumPy.
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """lazy_matrix_mul(m_a, m_b)

    Args:
        m_a list: a list of lists(matrix)
        m_b list: a list of lists(matrix)

    Returns:
        list|matrix: a list of lists(matrix)
    """
    return numpy.matmul(m_a, m_b)
