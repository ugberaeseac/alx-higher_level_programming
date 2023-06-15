#!/usr/bin/python3

def best_score(a_dictionary):
    max_value = 0
    max_key = 0

    if (a_dictionary):
        for key, value in a_dictionary.items():
            if value > max_value:
                max_value = value
                max_key = key
        return (max_key)

    else:
        return None
