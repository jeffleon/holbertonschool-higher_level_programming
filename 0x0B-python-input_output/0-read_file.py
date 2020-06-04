#!/usr/bin/python3
"""
Handle Files
"""


def read_file(filename=""):
    """
    Function to print a File
    """
    with open(filename) as f:
        for line in f:
            print(line, end="")
    f.close
