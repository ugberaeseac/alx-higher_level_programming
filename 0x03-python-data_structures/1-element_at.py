#!/usr/bin/python3

def element_at(my_list, idx):
    count = len(my_list)
    if (idx < 0):
        return (None)
    elif (idx > count):
        return (None)
    else:
        return (my_list[idx])
