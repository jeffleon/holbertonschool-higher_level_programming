#!/usr/bin/python3
"""
Handle Files
"""


def write_file(filename="", text=""):
    """
    Write in a File
    """
    with open(filename, "w+") as f:
        f.write(text)
    return len(text)
