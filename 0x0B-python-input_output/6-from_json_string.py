#!/usr/bin/python3
"""
Handle Files
"""
import json


def from_json_string(my_str):
    """
    Return a cast to data struct in python
    """
    return json.loads(my_str)
