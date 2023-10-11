#!/usr/bin/python3


""" a function that returns True if the object is exactly
an instance of the specified class"""


def is_same_class(obj, a_class):
    """check for obj in same class"""
    return type(obj) is a_class
