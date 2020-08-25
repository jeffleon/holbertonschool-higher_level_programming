#!/usr/bin/python3
""" the urllib request"""
import urllib.request
import urllib.parse
import sys
import urllib.error

if __name__ == "__main__":
    """ get header with the name X-Request-Id """
    try:
        url = urllib.request.Request(sys.argv[1])
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
