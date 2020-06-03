#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """
    Area
    """
    pass

    def area(self):
        """
        Area exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validator 
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """
    def __init__(self, width, height):
        """
        Initializes
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
