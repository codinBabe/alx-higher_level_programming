#!/usr/bin/python3


""" a class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class that inherit from Rectangle"""
    def __init__(self, size):
        """initialize private attribute"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of a square"""
        return self.__size ** 2
