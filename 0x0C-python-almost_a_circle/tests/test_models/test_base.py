import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Base(unittest.TestCase):
    def test_save_to_file(self):
        """Tests for save_to_file method"""
        rectangle_obj = Rectangle(9, 8, 1, 2, 23)
        square_obj = Square(4, 5, 6, 21)

    def test_from_json_string(self):
        """Tests for from_json_string method"""
        with self.assertRaises(TypeError):
            Base.from_json_string()
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(''), [])

    def test_to_json_string(self):
        """Tests for to_json_string method"""
        res = Base.to_json_string([])
        self.assertEqual(type(res), str)
        self.assertEqual(Base.to_json_string(None), '[]')
        self.assertEqual(Base.to_json_string(1), '1')
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])
