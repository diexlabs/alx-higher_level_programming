#!/usr/bin/python3
'''A module that appends to a file'''


def append_write(filename="", text=""):
    '''appends to the end of a file
    Args:
        filename (str) - the name of the file
        text (str) - the text string to append

    Return total - the number of characters written
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        total = f.write(text)

    return total
