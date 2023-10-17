import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 2)

    def test_attributes_with_id(self):
        r = Rectangle(10, 20, 5, 5, 42)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)
        self.assertEqual(r.id, 42)

    def test_width_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 20)

    def test_width_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(0, 20)

    def test_height_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "20")

    def test_height_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, -20)

    def test_x_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, "5")

    def test_x_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, -5)

    def test_y_type_error(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, 20, 5, "5")

    def test_y_value_error(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10, 20, 5, -5)

    def test_area(self):
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(2, 2)
        expected_output = "##\n##\n"
        with io.StringIO() as mock_stdout:
            sys.stdout = mock_stdout
            r.display()
            sys.stdout = sys.__stdout__
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        r = Rectangle(10, 20, 5, 5, 42)
        expected_str = "[Rectangle] (42) 5/5 - 10/20"
        self.assertEqual(str(r), expected_str)

    def test_update_args(self):
        r = Rectangle(10, 20, 5, 5, 42)
        r.update(1, 15, 25, 10, 10)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_update_kwargs(self):
        r = Rectangle(10, 20, 5, 5, 42)
        r.update(width=15, height=25, x=10, y=10, id=1)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)

    def test_update_args_and_kwargs(self):
        r = Rectangle(10, 20, 5, 5, 42)
        r.update(1, 15, 25, 10, 10, id=99)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 25)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)  # Args take precedence

    def test_to_dictionary(self):
        r = Rectangle(10, 20, 5, 5, 42)
        expected_dict = {'id': 42, 'width': 10, 'height': 20, 'x': 5, 'y': 5}
        self.assertEqual(r.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
