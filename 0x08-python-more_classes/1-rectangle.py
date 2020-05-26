#!/bin/usr/python3
"""
    Module of Rectangule
"""


class Rectangle:
    """ Class of Rectangule """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter of width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width >= 0:
            self.__width = width
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Getter of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter of height"""
        if type(height) is not int:
            raise TypeError("width must be an integer")
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("width must be >= 0")
