#!/usr/bin/python3
"""This module defines a text file-append function"""


def append_write(filename="", text=""):
    """append a string to a UTF8 text file"""
    with open(filename, "a", encoding="utf-8") as f:
        content = f.write(text)
    return(content)
