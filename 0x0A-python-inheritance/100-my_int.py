#!/usr/bin/python3
"""
Class Myint
"""


class MyInt(int):
    """
    Init my int
    """
    def __init__(self, num):
        self.num = num

    def __eq__(self, numero):
        return False

    def __ne__(self, numero):
        return True
