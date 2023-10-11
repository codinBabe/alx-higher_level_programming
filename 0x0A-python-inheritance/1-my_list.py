#!/usr/bin/python3


"""a class MyList that inherits from list"""


class MyList(list):
    """a subclass of list class"""
    def __init__(self):
        """initialize mylist"""
        super().__init__()

    def print_sorted(self):
        """funtion that print sorted list"""
        print(sorted(self))
