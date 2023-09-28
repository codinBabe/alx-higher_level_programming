#!/usr/bin/python3


"""a function that prints an integer with "{:d}".format()."""


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
