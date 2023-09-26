#!/usr/bin/python3


"""class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """square class with private and public attribute"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """area of a square"""
        return self.__size * self.__size
