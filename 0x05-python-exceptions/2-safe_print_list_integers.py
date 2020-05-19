#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in my_list
    try:
        print("{:d}".format(i), end='')
        counter += 1
    except (TypeError, valueError):
        pass
    print("")
    return counter
