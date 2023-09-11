#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a1 = tuple_a + (0, 0)
    b2 = tuple_b + (0, 0)

    res1 = 0
    res2 = 0

    res1 += a1[0] + b2[0]
    res2 += a1[1] + b2[1]

    return (res1, res2)
