#!/usr/bin/python3

def matrix_divided(matrix, div):
    '''
    This function takes a list (matrix) and an integer as input.
    args:
        matrix (list): first argument
        div (int): second argument
    Return:
        the result of each element in the matrix divided by div
    '''
    result_matrix = []
    types = [float, int]
    length = len(matrix[0])

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(0, len(matrix)):
        new_row = []
        if len(matrix[i]) != length:
            raise ValueError('Each row of the matrix must have the same size')
        for j in range(0, len(matrix[i])):
            if type(matrix[i][j]) not in types:
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats")
            result = round(float(matrix[i][j] / div), 2)
            new_row.append(result)
        result_matrix.append(new_row)

    return result_matrix
