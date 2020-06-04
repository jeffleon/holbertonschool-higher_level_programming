#!/usr/bin/python3
def number_of_lines(filename=""):
    num = 0
    with open(filename) as f:
        for line in f:
            num += 1
    f.close
    return num


def read_lines(filename="", nb_lines=0):
    lines = number_of_lines(filename)
    if nb_lines <= 0:
        nb_lines = lines
    with open(filename) as f:
        for n, line in enumerate(f):
            if n == nb_lines:
                break
            print(line)
    f.close()
