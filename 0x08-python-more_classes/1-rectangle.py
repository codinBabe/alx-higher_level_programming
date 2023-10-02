#!/usr/bin/python3


"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """a class rectangle with private attribute"""

    def __init__(self, width=0, height=0):
        """recetangle attribute"""
        self.width = width
        self.height = height

    @property
    def width(self, width):
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
    def height(self, height):
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
