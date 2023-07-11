#!/usr/bin/python3

"""
Module: 5-save_to_json_file
writes an object to a text file
using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
    write object to text file
    """
    with open(filename, mode='w', encoding='utf-8') as myFile:
        myFile.write(json.dumps(my_obj))
