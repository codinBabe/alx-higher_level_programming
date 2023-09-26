#!/usr/bin/python3


"""a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """square class with attributes"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        """to retrieve attribute"""
        return self.__size

    @property
    def position(self):
        """to retrieve position attribute"""
        return self.__position

    @size.setter
    def size(self, value):
        """to set it value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """to set attribute position"""
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(val, int) and val >= 0 for val in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area of a square"""
        return self.__size * self.__size

    def my_print(self):
        """print the square with characters"""
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)
