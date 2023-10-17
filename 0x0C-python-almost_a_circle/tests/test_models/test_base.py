import unittest
import json
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_init(self):
        """Test when id is provided"""
        b = Base(10)
        self.assertEqual(b.id, 10)

        """Test when id is not provided"""
        b = Base()
        self.assertEqual(b.id, 1)

        """Test with multiple instances"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 3)

    def test_to_json_string(self):
        """Test when list_dictionaries is empty"""
        self.assertEqual(Base.to_json_string([]), "[]")

        """Test when list_dictionaries contains dictionaries"""
        r = Rectangle(10, 20)
        r_dict = r.to_dictionary()
        s = Square(5)
        s_dict = s.to_dictionary()
        json_str = Base.to_json_string([r_dict, s_dict])
        expected = json.dumps([r_dict, s_dict])
        self.assertEqual(json_str, expected)

        """Test when list_dictionaries is None"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_save_to_file(self):
        """Test with an empty list"""
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

        """Test with a list of Rectangle instances"""
        r1 = Rectangle(10, 20, 1, 2, 7)
        r2 = Rectangle(5, 5, 3, 4, 8)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            data = file.read()
            self.assertEqual(data, Base.to_json_string([r1.to_dictionary(), r2.to_dictionary()]))

        """Test with a list of Square instances"""
        s1 = Square(5, 1, 2, 9)
        s2 = Square(3, 3, 4, 10)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, Base.to_json_string([s1.to_dictionary(), s2.to_dictionary()]))

    def test_from_json_string(self):
        """Test when json_string is empty"""
        self.assertEqual(Base.from_json_string(""), [])

        """Test when json_string is None"""
        self.assertEqual(Base.from_json_string(None), [])

        """Test when json_string contains JSON data"""
        json_str = '[{"id": 1, "width": 10, "height": 20, "x": 1, "y": 2}, ' \
                   '{"id": 2, "size": 5, "x": 3, "y": 4}]'
        lst = Base.from_json_string(json_str)
        self.assertTrue(type(lst) is list)
        self.assertEqual(lst[0]['id'], 1)
        self.assertEqual(lst[1]['size'], 5)

    def test_create(self):
        """Test creating a Rectangle"""
        r = Rectangle(10, 20, 1, 2, 7)
        r_dict = r.to_dictionary()
        r_copy = Rectangle.create(**r_dict)
        self.assertIsNot(r, r_copy)
        self.assertEqual(r, r_copy)

        """Test creating a Square"""
        s = Square(5, 1, 2, 9)
        s_dict = s.to_dictionary()
        s_copy = Square.create(**s_dict)
        self.assertIsNot(s, s_copy)
        self.assertEqual(s, s_copy)

    def test_load_from_file(self):
        """Test loading from a nonexistent file"""
        result = Rectangle.load_from_file()
        self.assertEqual(result, [])

        """Test loading from a file with data"""
        r1 = Rectangle(10, 20, 1, 2, 7)
        r2 = Rectangle(5, 5, 3, 4, 8)
        Rectangle.save_to_file([r1, r2])
        result = Rectangle.load_from_file()
        self.assertTrue(type(result) is list)
        self.assertEqual(len(result), 2)

        """Test loading from a file with Square data"""
        s1 = Square(5, 1, 2, 9)
        s2 = Square(3, 3, 4, 10)
        Square.save_to_file([s1, s2])
        result = Square.load_from_file()
        self.assertTrue(type(result) is list)
        self.assertEqual(len(result), 2)

if __name__ == "__main__":
    unittest.main()
