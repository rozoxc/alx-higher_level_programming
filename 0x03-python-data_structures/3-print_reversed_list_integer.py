#!/bin/usr/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list) - 1
    i = 0
    while l >= i:
        print("{:d}".format(my_list[l]))
        l = l - 1
