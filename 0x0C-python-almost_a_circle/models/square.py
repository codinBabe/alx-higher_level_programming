#!/usr/bin/python3


"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A class square the inherit rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string represntation of square"""
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """getter for class square"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """a public method upadte for square"""
        attr_names = ["id", "size", "x", "y"]
        if args:
            for i in range(len(args)):
                setattr(self, attr_names[i], args[i])
        else:
            for key, value in kwargs.items():
                if key in attr_names:
                    setattr(self, key, value)

    def to_dictionary(self):
        """convert square to dictionary"""
        squ_dict = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return squ_dict
