import unittest
from io import StringIO
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_valid_creation(self):
        """Test valid creation of Square"""
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)

    def test_default_id(self):
        """Test Square creation with default id"""
        s = Square(2)
        self.assertEqual(s.id, 2)

    def test_valid_update_args(self):
        """Test valid update with *args"""
        s = Square(3)
        s.update(1, 5, 2, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_valid_update_kwargs(self):
        """Test valid update with **kwargs"""
        s = Square(3)
        s.update(x=2, size=5, y=1, id=1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 1)

    def test_area(self):
        """Test area calculation"""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_display(self):
        s = Square(2)
        expected_output = "##\n##\n"
        with StringIO() as mock_stdout:
            s.display()
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """Test string representation"""
        s = Square(3, 1, 2, 7)
        self.assertEqual(str(s), "[Square] (7) 1/2 - 3")

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        s = Square(2, 1, 2, 7)
        d = s.to_dictionary()
        self.assertEqual(d, {'id': 7, 'size': 2, 'x': 1, 'y': 2})

    def test_setter_and_getter(self):
        """Test size setter and getter"""
        s = Square(4)
        s.size = 6
        self.assertEqual(s.size, 6)
        self.assertEqual(s.width, 6)
        self.assertEqual(s.height, 6)

if __name__ == '__main__':
    unittest.main()
