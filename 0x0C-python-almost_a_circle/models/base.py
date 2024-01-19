#!/usr/bin/python3

class Base:
    '''private attribute'''
    __nb_objects = 0

    def __init__(self, id=None):
        if id is None:
            # Generate a unique ID for the object
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
