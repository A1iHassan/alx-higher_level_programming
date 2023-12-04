#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("")
    else:
        for i in matrix:
            print(*(x for x in i), sep=" ", end="\n")
