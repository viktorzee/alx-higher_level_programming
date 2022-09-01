#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for val in range(len(matrix)): 
        new_matrix[val] = list(lambda x: x ** 2, matrix[val])

    return (new_matrix)
