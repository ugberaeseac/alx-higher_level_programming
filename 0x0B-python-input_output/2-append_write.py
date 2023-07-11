#!/usr/bin/python3

"""
Module 2-append_write
appends a string to the end of a text file
returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    append string and return character added
    """
    with open(filename, mode='a', encoding='utf-8') as myFile:
        return (myFile.write(text))
