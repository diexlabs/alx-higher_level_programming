#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div


def main(argv: list):
    if len(argv) != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        sys.exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operators = {'+': add, '-': sub, '*': mul, '/': div}
    op = argv[2]

    if op not in operators.keys():
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    print('{} {} {} = {}'.format(a, op, b, operators[op](a, b)))


if __name__ == "__main__":
    main(sys.argv)
