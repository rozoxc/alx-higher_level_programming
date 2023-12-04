#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        j = 0
        for j in range(0, len(matrix[j])):
            print("{}".format(matrix[i][j]), end=" ")
            print()
