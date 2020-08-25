#!/usr/bin/python3
""" the urllib request"""
import requests
import sys

if __name__ == "__main__":
    """ API JSON RESULT """
    try:
        query = {"q": sys.argv[1]}
        res = requests.post("http://0.0.0.0:5000/search_user", query)
        if res.headers.get('content-type') != 'application/json':
            raise TypeError
        if res.json():
            print("[{}] {}".format(res.json()["id"], res.json()["name"]))
        else:
            print("No result")
    except IndexError:
        print("No result")
    except TypeError:
        print("Not a valid JSON")
