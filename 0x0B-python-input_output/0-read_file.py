#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    try:
        """Print the contents of a UTF8 text file to stdout."""
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(filename + " is not found")
    except PermissionError:
        print("you don't have permission to read " + filename)
