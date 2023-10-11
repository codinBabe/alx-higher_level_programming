#!/usr/bin/python3


"""json module"""
import json
"""a function that returns the JSON representation of an object (string)"""


def to_json_string(my_obj):
    """This function return JSON object
    :param:my_obj - object to return
    """
    return json.dumps(my_obj)

