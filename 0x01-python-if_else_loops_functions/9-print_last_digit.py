#!/usr/bin/python3
def print_last_digit(number):
    if (number > 0):
        last_number = number % 10
    elif (number == 0):
        last_number = 0
    else:
        last_number = (number * -1) % 10
    print(last_number, end="")
    return (last_number)
