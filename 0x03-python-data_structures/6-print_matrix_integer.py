#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for n in r:
            print("{:d}".format(n), end=" " if n != r[-1] else "")
        print()
