#!/usr/bin/python3


"""a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """a class with property"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """to retrieve the attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set the attribute"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of a square"""
        return self.__size * self.__size
