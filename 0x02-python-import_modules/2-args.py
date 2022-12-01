#!/usr/bin/python3

import sys


def main(li: list):
    if len(li) == 0:
        print('0 arguments.')
    elif len(li) == 1:
        print('1 argument:')
    else:
        print('{} arguments:'.format(len(li)))

    for index, arg in enumerate(li):
        print('{}: {}'.format(index + 1, arg))

    return


if __name__ == "__main__":
    main(sys.argv[1:])
