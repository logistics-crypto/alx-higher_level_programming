#!/usr/bin/python3
""" Module that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """ Function that prints My name

    Args:
        first_name (str): first name
        last_name (str): last name
    Returns:
        None

    Raises:
        TypeError: if first_name or last_name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
