#!/usr/bin/python3
"""module for project 0x07
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): Matrix of ints or floats.
        div (int or float): Divisor.

    Returns:
        list of lists: New matrix with elements rounded to 2 decimal places.
    """
    if (not all(isinstance(row, list) and
                all(isinstance(e, (int, float)) for e in r) for r in matrix)):
        raise TypeError("""matrix must be a matrix \
                        (list of lists) of ints/floats""")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or div == 0:
        raise TypeError("div must be a non-zero number")

    result_matrix = [[round(e / div, 2) for e in row] for row in matrix]
    return result_matrix
