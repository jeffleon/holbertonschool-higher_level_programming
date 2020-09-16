#!/usr/bin/python3
"""
Handle Json
"""
import json


def load_from_json_file(filename):
    """
    Return a obj_json
    """
    with open(filename) as f:
        for line in f:
            obj = json.loads(line)
    return obj
