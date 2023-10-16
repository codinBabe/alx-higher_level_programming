#!/usr/bin/python3


"""unittest for class Base"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_valid_creation(self):
        """test for valid creation"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_custom_id(self):
        """test for custom id"""
        b1 = Base(10)
        self.assertEqual(b1.id, 10)

        b2 = Base(42)
        self.assertEqual(b2.id, 42)

if __name__ == '__main__':
    unittest.main()

class TestBaseStaticMethod(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        """Test when list_dictionaries is an empty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

    def test_to_json_string_none(self):
        """Test when list_dictionaries is None"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

    def test_to_json_string_with_data(self):
        """Test with a list of dictionaries"""
        data = [{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]
        json_string = Base.to_json_string(data)

        """Verify that the JSON string contains the expected data"""
        expected_json = '[{"id": 1, "name": "John"}, {"id": 2, "name": "Jane"}]'
        self.assertEqual(json_string, expected_json)

if __name__ == '__main__':
    unittest.main()
