#!/usr/bin/python3
"""
Handle Files
"""


def read_lines(filename="", nb_lines=0):
    """
    Read a especific lines of code
    """
    with open(filename) as f:
        lines = f.readlines()
        if nb_lines <= 0 or nb_lines >= len(lines):
            for line in lines:
                print(line, end='')
        else:
            for no_line in range(nb_lines):
                print(lines[no_line], end='')
