import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Rectangle(unittest.TestCase):

    def test_area_validations(self):
        """Tests for area method"""
        rectangle_obj2 = Rectangle(8, 2, 1, 1, 7)
        self.assertEqual(rectangle_obj2.area(), 16)
        with self.assertRaises(TypeError):
            rectangle_obj2.area(45)

    def test__str__validations(self):
        """Tests for __str__ method"""
        rectangle_ob4 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(rectangle_ob4.__str__(), '[Rectangle] (12) 2/1 - 4/6')

    def test_update_validations(self):
        """Tests for update method"""
        rectangle_obj5 = Rectangle(1, 1, 1, 1, 1)
        self.assertEqual(rectangle_obj5.update(), None)
        self.assertEqual(rectangle_obj5.id, 1)

    def test_to_dictionary_validations(self):
        """Tests for to_dictionary method"""
        rectangle_obj6 = Rectangle(4, 2, 1, 1, 5)
        self.assertEqual(type(rectangle_obj6.to_dictionary()), dict)
        aux = {'id': 5, 'height': 2, 'width': 4, 'x': 1, 'y': 1}
        self.assertTrue(rectangle_obj6.to_dictionary() == aux)
