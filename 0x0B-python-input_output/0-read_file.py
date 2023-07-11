#!/usr/bin/python3

"""
Module: 0-read_file
Reads a file and print to
stdout
"""


def read_file(filename=""):
    """
    read and print file to stdout
    """

    with open(filename, mode='r', encoding='utf-8') as myFile:
        print(myFile.read(), end="")
