#!/usr/bin/python3
""" the urllib request"""
import requests

if __name__ == "__main__":
    response = requests.get("https://intranet.hbtn.io/status")
    print(response.headers['X-Request-Id'])
