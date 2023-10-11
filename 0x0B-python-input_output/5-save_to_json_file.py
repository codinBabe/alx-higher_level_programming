#!/usr/bin/python3


"""json string"""
import json
"""json module"""


def save_to_json_file(my_obj, filename):
    """a function that writes an Object to a text file,
    using a JSON representation"""

    data = json.dumps(my_obj)
    with open(filename, 'w') as file:
        file.write(data)
