#!/usr/bin/python3


"""A class Base"""
import json


class Base:
    """a class with private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return dictionary to json"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """json string to file"""
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])
        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """return a list of instances"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as file:
                data = file.read()
                if not data:
                    return []

                list_dict = cls.from_json_string(data)
                insta = [cls.create(**d) for d in list_dict]
                return insta
        except FileNotFoundError:
            return []
