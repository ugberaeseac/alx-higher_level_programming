#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    if(my_string):
        for i in my_string:
            if (i != 'c' and i != 'C'):
                new_string += i

        return(new_string)
    else:
        return (my_string)
