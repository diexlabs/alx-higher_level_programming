#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    highest = my_list[0]
    for curr in my_list:
        if curr > highest:
            highest = curr

    return highest
