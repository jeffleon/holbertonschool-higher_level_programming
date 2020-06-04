#!/usr/bin/python3
def number_of_lines(filename=""):
    num = 0
    with open(filename) as f:
        for line in f:
            num += 1
    f.close
    return num
