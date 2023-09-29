#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
Must use urllip package
Must use a with statement
Not allowed to import any packages other than urllib
"""


import urllib.request


if __name__ == '__main__':
    htmlRequest = urllib.request.Request('https://alx-intranet.hbtn.io/status')
    with urllib.request.urlopen(htmlRequest) as response:
        htmlBody = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(htmlBody)))
        print('\t- content: {}'.format(htmlBody))
        print('\t- utf8 content: {}'.format(htmlBody.decode('utf-8')))
