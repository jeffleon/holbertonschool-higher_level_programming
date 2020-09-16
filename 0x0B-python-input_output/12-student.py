#!/usr/bin/python3
"""
Class Student
"""


class Student:
    """
    Constructor Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Attributes
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a Dictionary
        """
        if attrs is None:
            return self.__dict__
        dic = dict()
        for atr in attrs:
            if atr in self.__dict__:
                dic[atr] = self.__dict__[atr]
        return dic
