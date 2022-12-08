#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    nmatrix = []
    for row in matrix:
        nmatrix.append(list(map(lambda i: i*i, row)))
    return nmatrix
