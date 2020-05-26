#!/bin/usr/python3
class Rectangle:
    """ Class Rectangule """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter width"""
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width >= 0:
            self.__width = width
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Getter height"""
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height >= 0:
            self.__height = height
        else:
            raise ValueError("height must be >= 0")
