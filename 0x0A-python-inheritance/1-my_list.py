#!/usr/bin/python3

"""
Module: 1-my_list
A child class inherited from class list
that prints the list in ascending sort
"""


class MyList(list):
    """
    child class inherited from list

    Methods:
        print_sorted(self)
    """
    def print_sorted(self):
        """ print sorted list in ascending order """
        print(sorted(self))
