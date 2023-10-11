#!/usr/bin/python3


"""a function that returns True or false if the object is an instance of,
or if the object is an instance of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """this function checks instance of obj"""
    return isinstance(obj, a_class)
