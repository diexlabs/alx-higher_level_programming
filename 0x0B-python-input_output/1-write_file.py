#!/usr/bin/python3
'''A module for a function that write to a file'''


def write_file(filename="", text=""):
    '''write a text string to file
    
    Args:
        filename (str) - the name of the file
        text (str) - text string to write
    
    Return:
        total (int) - the total number of character written
    '''
    with open(filename, 'w', encoding='utf-8') as f:
        total = f.write(text)

    return total
