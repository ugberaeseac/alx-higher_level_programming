#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for i in str:
        if (ord(i) > 96 and ord(i) < 123):
            upper = upper + (chr(ord(i) - 32))
        else:
            upper = upper + i
    print("{}".format(upper))
