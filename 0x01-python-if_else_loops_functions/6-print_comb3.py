#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1, 10):
        if (i < j and i < 8):
            print("{}{}".format(i, j), end=", ")
        elif (i < j and i == 8):
            print("{}{}".format(i, j))
