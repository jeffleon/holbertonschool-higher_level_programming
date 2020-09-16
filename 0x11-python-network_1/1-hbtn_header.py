#!/usr/bin/python3
""" the urllib request"""
import urllib.request
import sys
if __name__ == "__main__":
    """ get header with the name X-Request-Id """
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
