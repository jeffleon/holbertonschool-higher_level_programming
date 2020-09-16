

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMax_integer(unittest.TestCase):
    def testMax_integer(self):
        self.assertAlmostEqual(max_integer([1,2,3,4]), 4)
        self.assertAlmostEqual(max_integer([]),None)
    def testMax_integer_Values(self):
        self.assertRaises(TypeError, max_integer, [1, 34, 5, 'u'])
