#!/usr/bin/python3
def magic_string(n = {'counter': 0}):
    n['counter'] += 1
    return "Holberton, " * (n['counter'] -1) + "Holberton"
