#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(matrix) > 1:
            for j in i:
                print("{:d}".format(j), end=" " if j != i[-1] else "")
            print()
        else:
            print()
