#!/usr/bin/python3
"""
Python Module matrix_divided
Dividing individual element(int or float type) of a matrix by a number
"""


def matrix_divided(matrix, div):
    """matrix_divided(matrix, div)

    Args:
        matrix (list): must be a list of lists of integers or
        floats, otherwise raise a TypeError
        div (int|float):  must be a number (integer or float),
        otherwise raise a TypeError

    Raises:
        TypeError: Raise if matrix not a matrix (list of lists)
        of integers/floats.
        TypeError: Raise if Each row of the matrix must have the same size.
        TypeError: Raised if div is not a number (integer or float).
        ZeroDivisionError: Raised if div is not a number(int|float)

    Returns:
        matrix(list of list): Returns a new matrix, a result of
        dividing the previous matrix by the div and rounded to 2 decimal places
    """

    if len(matrix) == 0 or not isinstance(matrix, list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        for item in row:
            if type(item) is not int and type(item) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_size = []
    for row in matrix:
        row_size.append(len(row))
    if not all(item == row_size[0] for item in row_size):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(x / div, 2) for x in row] for row in matrix]

    return new_matrix
