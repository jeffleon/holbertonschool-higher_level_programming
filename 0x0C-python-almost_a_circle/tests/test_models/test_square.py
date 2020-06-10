#!/usr/bin/python3
"""Unittest for Rectangle"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class test_Square(unittest.TestCase):
    def test_area_validations(self):
        """Tests for area method"""
        square_obj2 = Square(2, 10, 0, 3)
        self.assertEqual(square_obj2.area(), 4)
        with self.assertRaises(TypeError):
            square_obj2.area(45)

    def test__str__validations(self):
        """Tests for __str__ method"""
        square_obj3 = Square(10, 2, 1, 1)
        self.assertEqual(square_obj3.__str__(), '[Square] (1) 2/1 - 10')

    def test__str__validations(self):
        """Tests for __str__ method"""
        square_obj3 = Square(10, 2, 1, 1)
        self.assertEqual(square_obj3.__str__(), '[Square] (1) 2/1 - 10')
        square_obj33 = Square(9, 8, 4, 10)
        self.assertEqual(square_obj33.__str__(), '[Square] (10) 8/4 - 9')

    def test_to_dictionary_validations(self):
        """Tests for to_dictionary method"""
        square_obj7 = Square(4, 2, 1, 6)
        aux = {'id': 6, 'size': 4, 'x': 2, 'y': 1}
        self.assertTrue(square_obj7.to_dictionary() == aux)
        aux['size'] = 9
        self.assertFalse(square_obj7.to_dictionary() == aux)
