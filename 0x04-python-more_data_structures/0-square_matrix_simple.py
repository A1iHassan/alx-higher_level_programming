#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[i[x]**2 for x in range(len(i))] for i in matrix]
    return new
