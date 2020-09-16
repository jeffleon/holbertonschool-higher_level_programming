#!/usr/bin/python3
"""
Handle Files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write with json style
    """
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
