#!/usr/bin/python3
"""
Class Inherits_from
"""


def inherits_from(obj, a_class):
    """
    Return True is not a type but isintastance
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
