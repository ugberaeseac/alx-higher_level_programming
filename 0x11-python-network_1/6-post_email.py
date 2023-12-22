#!/usr/bin/python3
"""
given the URL and email, send POST request to URL
"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    mail = {'email': argv[2]}
    response = requests.post(url, data=mail)
    print(response.text)
