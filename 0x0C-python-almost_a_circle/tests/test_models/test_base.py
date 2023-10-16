#!/usr/bin/python3


"""unittest for class Base"""


import unittest
import os
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

class TestBaseClassMethod(unittest.TestCase):
    def test_save_to_file_with_data(self):
        """Test saving data to a file"""
        class Rectangle(Base):
            pass

        """Create instances to save to a file"""
        r1 = Rectangle(1)
        r2 = Rectangle(2)
        r3 = Rectangle(3)

        """Save the instances to a file"""
        Rectangle.save_to_file([r1, r2, r3])

        """Verify that the file exists and contains the expected data"""
        with open("Rectangle.json", "r") as file:
            data = file.read()
            expected_data = '[{"id": 1}, {"id": 2}, {"id": 3}]'
            self.assertEqual(data, expected_data)

    def test_save_to_file_with_empty_list(self):
        """Test saving an empty list to a file"""
        class Square(Base):
            pass

        """Save an empty list to a file"""
        Square.save_to_file([])

        """ Verify that the file exists and contains "[]" """
        with open("Square.json", "r") as file:
            data = file.read()
            self.assertEqual(data, "[]")

if __name__ == '__main__':
    unittest.main()

class TestBaseClassMethod(unittest.TestCase):
    def test_create_rectangle(self):
        """Test creating a Rectangle instance using the create method"""
        rectangle_dict = {'id': 1, 'width': 4, 'height': 5, 'x': 0, 'y': 0}
        rectangle_instance = Rectangle.create(**rectangle_dict)

        """Verify that the instance has the expected attributes"""
        self.assertEqual(rectangle_instance.id, 1)
        self.assertEqual(rectangle_instance.width, 4)
        self.assertEqual(rectangle_instance.height, 5)
        self.assertEqual(rectangle_instance.x, 0)
        self.assertEqual(rectangle_instance.y, 0)

    def test_create_square(self):
        """Test creating a Square instance using the create method"""
        square_dict = {'id': 2, 'size': 3, 'x': 1, 'y': 2}
        square_instance = Square.create(**square_dict)

        """Verify that the instance has the expected attributes"""
        self.assertEqual(square_instance.id, 2)
        self.assertEqual(square_instance.size, 3)
        self.assertEqual(square_instance.x, 1)
        self.assertEqual(square_instance.y, 2)

if __name__ == '__main__':
    unittest.main()

class TestBaseClassMethod(unittest.TestCase):
    def test_from_json_string_empty(self):
        """Test with an empty JSON string"""
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        """Test with None as the JSON string"""
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_valid(self):
        """Test with a valid JSON string"""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        result = Base.from_json_string(json_string)
        expected_result = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


class TestBaseClassMethod(unittest.TestCase):
    def setUp(self):
        """Create a sample JSON file with data for testing"""
        self.sample_json_data = '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}]'
        with open("Rectangle.json", "w") as file:
            file.write(self.sample_json_data)

    def tearDown(self):
        """Remove the sample JSON file after testing"""
        os.remove("Rectangle.json")

    def test_load_from_file_rectangle(self):
        """Test loading instances of Rectangle from a JSON file"""
        instances = Rectangle.load_from_file()
        self.assertEqual(len(instances), 1)

        """Verify the attributes of the loaded instance"""
        self.assertEqual(instances[0].id, 1)
        self.assertEqual(instances[0].width, 4)
        self.assertEqual(instances[0].height, 5)
        self.assertEqual(instances[0].x, 0)
        self.assertEqual(instances[0].y, 0)

    def test_load_from_file_square(self):
        """Test loading instances of Square from a JSON file"""
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 0)  # File is empty, so no instances should be loaded

if __name__ == '__main__':
    unittest.main()
