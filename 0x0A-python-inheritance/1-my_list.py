#!/usr/bin/python3
"""
Class Mylist
"""
class MyList(list):
    """
    print a sorted list
    """
    def print_sorted(self):
        print(sorted(self))
