#!/usr/bin/python3

'''A module for a function that reads a file'''


def read_file(filename=""):
    '''reads all the contents of a file and prints
    to standard output

    Args:
        filename (str) - the name of file to read
    '''

    with open(filename) as f:
        while True:
            line = f.readline()
            if not line:
                break
            print(line, end='')
