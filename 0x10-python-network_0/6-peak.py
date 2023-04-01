#!/usr/bin/python3
'''function to find a peak value of a list of integers'''

def find_peak(list_of_integers):
    '''find the peak value of integers list'''
    integers = list_of_integers
    size = len(integers)
    mid_e = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_e = mid_e // 2
        if (mid < size - 1 and
                integers[mid] < integers[mid + 1]):
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid + mid_e // 2
        elif mid_e > 0 and integers[mid] < integers[mid - 1]:
            if mid_e // 2 == 0:
                mid_e = 2
            mid = mid - mid_e // 2
        else:
            return integers[mid]
