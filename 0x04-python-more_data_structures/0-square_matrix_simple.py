#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        arr_row = []
        for x in i:
            arr_row.append(x * x)
        new_matrix.append(arr_row)
    return new_matrix
