#!/usr/bin/python3


"""a function that adds 2 integers."""


def add_integer(a, b=98):
    """
    This function takes two arguments, 'a' and 'b', and adds
    them together.

    :param a: The first integer to be added.
    :type a: int or float
    :param b: The second integer to be added (default is 98).
    :type b: int or float
    :return: The sum of 'a' and 'b'.
    :rtype: int
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
