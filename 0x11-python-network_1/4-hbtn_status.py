#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Must use request package
Not allowed to import packages other than requests
"""


import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    httpResponse = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(httpResponse.text)))
    print("\t- content: {}".format(httpResponse.text))
