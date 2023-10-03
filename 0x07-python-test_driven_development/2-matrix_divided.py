#!/usr/bin/python3


"""a function that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """ This function divide a set of matrix list
    :param matrix: the matrix of type(int or float)
    :param div: the integer to div the matrix with of type(int or float)
    :return: the divided matrix of type(int or float)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)\
            for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of \
                integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    res = [[round(e / div, 2) for e in row] for row in matrix]
    return res

