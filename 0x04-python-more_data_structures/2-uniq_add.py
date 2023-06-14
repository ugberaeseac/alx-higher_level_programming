#!/usr/bin/python3

def uniq_add(my_list=[]):
    resultSum = 0
    toSet = set(my_list)
    for i in toSet:
        resultSum += i
    return (resultSum)
