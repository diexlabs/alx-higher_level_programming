#!/usr/bin/python3

def weight_average(my_list=[]):
    average = 0
    if not my_list:
        return average

    sum_weight = sum([item[1] for item in my_list])
    weighted = sum([item[0] * item[1] for item in my_list])
    average = weighted / sum_weight
    return average
