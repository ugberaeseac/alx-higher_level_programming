#!/usr/bin/python3
"""
must use the packages urllib and sys
manage urllib.error.HTTPError exceptions
print: Error code: followed by the HTTP status code
must use the with statement
"""


from sys import argv
import urllib.request
from urllib.error import HTTPError


if __name__ == "__main__":
    httpRequest = urllib.request.Request(argv[1])

    try:
        with urllib.request.urlopen(httpRequest) as response:
            htmlBody = response.read()
            print(htmlBody.decode("utf-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
