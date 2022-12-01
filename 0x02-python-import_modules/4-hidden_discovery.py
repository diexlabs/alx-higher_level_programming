#!/usr/bin/python3

import hidden_4


def main():
    for word in dir(hidden_4):
        if not word.startswith('__'):
            print(word)


if __name__ == "__main__":
    main()
