#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    aux = 0
    for i in my_list:
        if i >= aux:
            aux = i
    return aux
