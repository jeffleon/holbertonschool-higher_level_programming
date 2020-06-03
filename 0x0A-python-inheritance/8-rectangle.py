#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    Area
    """
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """


    def __init__(self, width, height):
        """
        Initializes the subclass
        """
        self.__width = width
        self.__height = height
