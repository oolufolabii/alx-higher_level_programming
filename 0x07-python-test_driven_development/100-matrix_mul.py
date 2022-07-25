#!/usr/bin/python3
"""Python Module matrix_mul
Multiplies two matrices and returns the result.
"""


def matrix_mul(m_a, m_b):
    """matrix_mul(m_a, m_b)

    Args:
        m_a (list of lists):  A 2D matrix to be multiplied
        m_b (list of lists):  A 2D matrix to be multiplied on.

    Raises:
        TypeError: m_a|m_b must be a list
        TypeError: m_a|m_b must be a list of lists
        ValueError: m_a|m_b can't be empyty
        TypeError: m_a|m_b should contain only integers or floats
        TypeError: each row of m_a & m_b must should be of the same size
        ValueError: m_a and m_b can't be multiplied

    Returns:
        list of list(matrix): return a new matrix, a result of m_a * m_b
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for item in m_a:
        if type(item) is not list:
            raise TypeError("m_a must be a list of lists")
    for item in m_b:
        if type(item) is not list:
            raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    for row in m_a:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("m_b should contain only integers or floats")

    row_length = []
    for row in m_a:
        row_length.append(len(row))
    if not all(item == row_length[0] for item in row_length):
        raise TypeError("each row of m_a must should be of the same size")
    row_length = []
    for row in m_b:
        row_length.append(len(row))
    if not all(item == row_length[0] for item in row_length):
        raise TypeError("each row of m_b must should be of the same size")

    a_column = 0
    for col in m_a[0]:
        a_column += 1
    b_row = 0
    for row in m_b:
        b_row += 1

    if a_column != b_row:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for x in range(len(m_b[0]))] for y in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
