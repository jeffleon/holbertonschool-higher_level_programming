#!/bin/usr/python3
"""Rectangle"""


class Rectangle:
    """Class Rectangule"""
    def __init__(self, width=0, height=0):
        """Constructor"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value >= 0:
            self.__width = value
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """Getter height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value >= 0:
            self.__height = value
        else:
            raise ValueError("height must be >= 0")
