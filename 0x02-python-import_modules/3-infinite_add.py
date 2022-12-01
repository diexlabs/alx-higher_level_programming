#!/usr/bin/python3

import sys


def main(li):
    res = 0
    for num in li:
        res += int(num)

    print(res)


if __name__ == "__main__":
    main(sys.argv[1:])
