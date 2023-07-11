#!/usr/bin/python3

"""
Module: 6-load_from_json_file
create an object from a JSON file
"""


import json


def load_from_json_file(filename):
    """
    create object from JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as myFile:
        return(json.loads(myFile.read()))
