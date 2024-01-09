#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """read filename."""
    with open(filename, 'r') as file:
        contents = file.read()
        print(contents)
        file.close()
