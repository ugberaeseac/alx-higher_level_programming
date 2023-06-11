#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = len(tuple_a)
    b = len(tuple_b)

    if (a < 1):
        c, d = (0, 0)
    elif (a == 1):
        c, d = (tuple_a[0], 0)
    elif (a >= 2):
        c, d = (tuple_a[0], tuple_a[1])

    if (b < 1):
        m, n = (0, 0)
    elif (b == 1):
        m, n = (tuple_b[0], 0)
    elif (b >= 2):
        m, n = (tuple_b[0], tuple_b[1])

    sum = (c + m, d + n)
    return (sum)
