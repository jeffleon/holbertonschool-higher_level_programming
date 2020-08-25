#!/usr/bin/python3
""" the urllib request"""
import requests
import sys
if __name__ == "__main__":
    """ get request for the header code """
    data = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data)
    print(response.text)
