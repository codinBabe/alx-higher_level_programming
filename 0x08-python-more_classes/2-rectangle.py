#!/usr/bin/python3


"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """a class rectangle with private attribute"""

    def __init__(self, width=0, height=0):
        """recetangle attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """modify the attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """modify the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """perimeter of a rectangle 2(w + h)"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)
