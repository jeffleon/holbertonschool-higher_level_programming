#!/usr/bin/python3
"""
Handle Files
"""
import json


def to_json_string(my_obj):
    """
    Return a Text File in format JSON
    """
    return json.dumps(my_obj)
