#!/usr/bin/python3


"""a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """This functin print first name and last name
    :param: first name of type string
    :param: last name of type string
    :return: both names of type string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    full_name = "{:s} {:s}".format(first_name, last_name)

    print("My name is", full_name)
