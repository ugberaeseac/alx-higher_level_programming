#!/usr/bin/python3

"""
Module: 8-classs_to_json
function that returns the dictionary description
with simple data structure
"""


def class_to_json(obj):
    """
    return the dictionary description
    """
    return (obj.__dict__)
