#!/usr/bin/python3
""" the urllib request"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    """ get header with the name X-Request-Id """
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        print(response.read())
