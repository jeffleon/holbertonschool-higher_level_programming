#!/usr/bin/python3
""" the urllib request"""
import requests
import sys
if __name__ == "__main__":
    """ get request for the header code """
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.text)
    else:
        print("Error code: {}".format(response.status_code))
