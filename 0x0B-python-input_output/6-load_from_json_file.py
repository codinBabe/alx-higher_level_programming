#!/usr/bin/python3


"""json object"""
import json
"""json module"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”"""

    with open(filename, 'r') as file:
        data = json.load(file)
    return data
