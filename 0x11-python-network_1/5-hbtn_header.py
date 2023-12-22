#!/usr/bin/python3
"""
given the URL and email, sends a request to the
URL and displays the value of the variable
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
