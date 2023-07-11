#!/usr/bin/python3
import json

"""
Module: 3-to_json_string
returns the JSON representation of an
object (string)
"""


def to_json_string(my_obj):
    """
    return JSON representation
    """
    return (json.dumps(my_obj))
