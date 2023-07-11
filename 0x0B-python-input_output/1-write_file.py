#!/usr/bin/python3

"""
Module: 1-write_file
function that writes a string to a text file
and return the number of characters written
"""


def write_file(file_name="", text=""):
    """
    write to file and return number of characters
    """
    with open(file_name, mode='w', encoding='utf-8') as myFile:
        return (myFile.write(text))
