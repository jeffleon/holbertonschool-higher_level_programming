#!/usr/bin/python3
def remove_char_at(str, n):
    aux = ""
    return str[:n] + str[n + 1:] if str is not None else aux
