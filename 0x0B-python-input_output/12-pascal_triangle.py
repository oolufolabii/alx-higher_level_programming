#!/usr/bin/python3
"""a function that returns a list of lists of integers
representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """pascal_triangle(n).

    Args:
        n: size of the triangle

    Returns: a list of list of integers
    """

    if n <= 0:
        return []

    lists = [[0 for num in range(i + 1)] for i in range(n)]
    lists[0] = [1]

    for i in range(1, n):
        lists[i][0] = 1
        for j in range(1, i + 1):
            if j < len(lists[i - 1]):
                lists[i][j] = lists[i - 1][j - 1] + lists[i - 1][j]
            else:
                lists[i][j] = lists[i - 1][0]
    return lists
