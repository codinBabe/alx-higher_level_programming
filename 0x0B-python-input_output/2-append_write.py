#!/usr/bin/python3


"""a function that appends a string at the end of a text file (UTF8) and \
        returns the number of characters written"""


def append_write(filename="", text=""):
    """This function appends text to a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)

        count = len(text)
    return count
