#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for r in matrix:
        new_r = []
        for num in r:
            new_r.append(num ** 2)
        new_matrix.append(new_r)
    return new_matrix
