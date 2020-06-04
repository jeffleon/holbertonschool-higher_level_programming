#!/usr/bin/python3
"""
Handle Files
"""


def class_to_json(obj):
    """
    Return a Dictionary with attributes
    """
    return obj.__dict__
