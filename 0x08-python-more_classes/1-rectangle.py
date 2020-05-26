#!/bin/usr/python3
""" Rectangle """


class Rectangle:
    """ Class Rectangule """
    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter width"""
        return self.__width

    @width.setter
    def width(self, val):
        """ Setter width"""
        if type(val) is not int:
            raise TypeError("width must be an integer")
        if val >= 0:
            self.__width = val
        else:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        """ Getter height"""
        return self.__height

    @height.setter
    def height(self, val):
        """ Setter height"""
        if type(val) is not int:
            raise TypeError("height must be an integer")
        if val >= 0:
            self.__height = val
        else:
            raise ValueError("height must be >= 0")
