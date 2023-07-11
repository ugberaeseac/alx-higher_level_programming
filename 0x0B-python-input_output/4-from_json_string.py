#!/usr/bin/python3

"""
Module: from-to_json_string
returns an object (Python data structure)
represented by JSON
"""


import json


def from_json_string(my_str):
    """
    returns object represented by JSON
    """
    return (json.loads(my_str))
