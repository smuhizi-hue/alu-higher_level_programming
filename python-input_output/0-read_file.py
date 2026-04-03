#!/usr/bin/python3
"""
This module contains a fuction that reads a text file and prints it to stduot.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
    """   
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
