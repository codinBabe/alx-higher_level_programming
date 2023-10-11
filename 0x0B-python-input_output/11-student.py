#!/usr/bin/python3


"""a class Student that defines a student by"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        """a public instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict represntation of a student"""
        data = {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
                }
        if attrs is None:
            return data
        else:
            att = {}
            for attr in attrs:
                if hasattr(self, attr):
                    att[attr] = getattr(self, attr)
            return att

    def reload_from_json(self, json):
        """replace all attribute of student intances"""
        for keys in json:
            setattr(self, keys, json[keys])
