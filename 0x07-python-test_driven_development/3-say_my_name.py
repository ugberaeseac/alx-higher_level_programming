#!/usr/bin/python3
"""
Module: 3-say_my_name
function that prints 'My name is <first_name> <last_name>'
raise exceptions is arguments passed is not a string
"""


def say_my_name(first_name, last_name=""):
    """
    Prints my name
    """
    if type(first_name) not in [str]:
        raise TypeError('first_name must be a string')

    elif type(last_name) not in [str]:
        raise TypeError('last_name must be a string')

    else:
        print("My name is {:s} {:s}".format(first_name, last_name))
