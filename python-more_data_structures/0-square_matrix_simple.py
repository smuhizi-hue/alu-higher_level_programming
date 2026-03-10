#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        # map() applies the lambda function to every item in the row
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
