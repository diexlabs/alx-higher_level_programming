#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    
    ret = list(map(lambda num: True if num % 2 == 0 else False, my_list))
    return ret
