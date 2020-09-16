#!/usr/bin/python3
"""
Handle Files
"""


def number_of_lines(filename=""):
    """
    Return the number of lines un file
    """
    num = 0
    with open(filename) as f:
        for line in f:
            num += 1
    f.close
    return num
