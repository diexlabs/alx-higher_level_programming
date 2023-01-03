#!/usr/bin/python3
"""A module for `say_my_name` function."""


def say_my_name(first_name, last_name=""):
    """Prints a string with <first_name> and <last_name>.

    Parameters:
        first_name (str): first name
        last_name (str): last name
    Return:
        None
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
