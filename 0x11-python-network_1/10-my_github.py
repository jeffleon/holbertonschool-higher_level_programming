#!/usr/bin/python3
""" the urllib request"""
import requests
import sys
if __name__ == "__main__":
    try:
        usr = sys.argv[1]
        psw = sys.argv[2]
        url = "https://api.github.com/user"
        res = requests.get(url, auth=(usr, psw))
        print(res.json()['id'])
    except:
        print("None")
