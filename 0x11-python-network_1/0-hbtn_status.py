#!/usr/bin/python3
""" the urllib request"""
import urllib.request
if __name__ == "__main__":
    """ the main request to intranet hbtn """
    with urllib.request.urlopen("https://intranet.hbtn.io/status") as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode()))
