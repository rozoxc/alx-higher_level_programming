#!/usr/bin/python3
def read_file(filename=""):
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print(contents)
    except FileNotFoundError:
        print(filename + " is not found")
    except PermissionError:
        print("you don't have permission to read " + filename)
