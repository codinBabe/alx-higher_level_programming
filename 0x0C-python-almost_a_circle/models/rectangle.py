#!/usr/bin/python3


"""the class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """a class rectangle with getter and setter private attribute"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """to retrieve attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """to initialise its value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """to retrieve attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """to initialise its value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """to retrieve attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """to initialise its value"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """to retrieve attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """to initialise its value"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """return area of rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for i in range(self.y):
            print()

        for i in range(self.height):
            for j in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """print string representation of rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        """update the class rectangle by adding public method"""
        attr_names = ["id", "width", "height", "x", "y"]

        for i, arg in enumerate(args):
            if i < len(attr_names):
                setattr(self, attr_names[i], arg)
