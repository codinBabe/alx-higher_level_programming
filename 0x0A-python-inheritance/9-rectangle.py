#!/usr/bin/python3


"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """an inherited rectangle class from basegeometry"""
    def __init__(self, width, height):
        """initialize private attributes"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """override BaseGeometry area"""
        return self.__width * self.__height

    def __str__(self):
        """string representation of Rectangle"""
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
