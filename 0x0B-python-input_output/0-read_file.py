#!/usr/bin/python3


"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """This function reads a file"""
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    print(data, end="")
