#!/usr/bin/python3

"""a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """square class with private attribute and exception"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
