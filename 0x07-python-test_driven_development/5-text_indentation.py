#!/usr/bin/python3
"""A module for `text_indentation` function."""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.

    Parameters (str): string text for formatting
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
