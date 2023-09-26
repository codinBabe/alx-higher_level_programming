#!/usr/bin/python3


"""a class Square that defines a square by: (based on 4-square.py)"""

class Square:
    """square class with attributes"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """to retrieve attribute"""
        return self.__size

    @size.setter
    def size(self, value):
        """to set it value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square with characters"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
