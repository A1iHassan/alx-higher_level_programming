#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = [[i[x]**2 for x in range(len(i) - 1)] for i in matrix]
