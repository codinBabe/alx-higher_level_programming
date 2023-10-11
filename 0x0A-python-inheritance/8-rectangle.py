#!/usr/bin/python3


"""a class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """an inherited rectangle class from basegeometry"""
    def __init__(self, width, height):
        self.__width = super().integer_validator("width", width)
        self.__height = super().integer_validator("height", height)
