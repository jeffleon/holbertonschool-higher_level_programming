#!/usr/bin/python3
"""
Handle a Files
"""


def append_write(filename="", text=""):
    """
    Write in append file
    """
    with open(filename, "a+") as f:
        f.write(text)
    return len(text)
