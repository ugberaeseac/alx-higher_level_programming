#!/usr/bin/python3

"""
Module: 3-to_json_string
returns the JSON representation of an
object (string)
"""


import json


def to_json_string(my_obj):
    """
    return JSON representation
    """
    return (json.dumps(my_obj))
