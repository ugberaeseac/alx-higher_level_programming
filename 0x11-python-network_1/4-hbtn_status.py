#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Must use request package
Not allowed to import packages other than requests
"""


import requests


if __name__ == "__main__":
    httpResponse = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(httpResponse.text)))
    print("\t- content: {}".format(httpResponse.text))
