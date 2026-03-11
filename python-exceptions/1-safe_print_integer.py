#!/usr/bin/python3
def safe_print_integer(value):
    """
    Safely prints an integer using "{:d}".format().

    Args:
        value: Can be any type (integer, string, etc.).

    Returns:
        True if value has been correctly printed (it means the value is an integer),
        Otherwise, returns False.
    """
    try:
        print("{:d}".format(value))
        return True
