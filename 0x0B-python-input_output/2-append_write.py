#!/usr/bin/python3

"""

"""


def append_write(filename="", text=""):
    """
    """
    with open(filename, mode='a', encoding='utf-8') as myFile:
        return (myFile.write(text))
