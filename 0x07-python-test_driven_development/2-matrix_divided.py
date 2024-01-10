#!/usr/bin/python3
"""module for project 0x07
"""


def matrix_divided(matrix, div):
    """devides elements of a matrixs by a certain number

    Args:
        matrix: given list of lists of the type int/float
        div: number to by devided by

    Return:
        list of divisions' results
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        for i in range(1, len(matrix)):
            if len(matrix[i]) != len(matrix[i - 1]):
                raise TypeError("Each row of the matrix must have the same size")

        for line in matrix:
            for element in line:
                if not isinstance(element, (int, float)):
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
        return [round(element / 2, 2) for element in line for line in matrix]
