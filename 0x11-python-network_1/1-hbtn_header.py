#!/usr/bin/python3
"""
Sends a request to URL and display the value
of the 'X-Request-Id' in the header of response
Must use urllib and sys packages
value of variable is different for each request
Must use a with statement
"""


from sys import argv
import urllib.request


if __name__ == '__main__':
    url = argv[1]
    httpRequest = urllib.request.Request(url)
    with urllib.request.urlopen(httpRequest) as response:
        htmlBody = response.getheader('X-Request-Id')
        print(htmlBody)
