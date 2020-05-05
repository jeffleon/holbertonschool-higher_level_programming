#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    aux = 0
    for i in my_list:
        if aux < i:
            aux = i
    return aux
