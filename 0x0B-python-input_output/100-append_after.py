#!/usr/bin/python3
"""
Function Append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function that add a new string determinates for a search
    """
    newline = []
    with open(filename, "r+") as f:
        for line in f:
            newline.append(line)
            if search_string in line:
                newline.append(new_string)
    f.close()
    with open(filename, "w") as f:
        f.write("".join(newline))
