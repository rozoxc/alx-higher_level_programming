#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0):
        return my_list
    for i in range(0, len(my_list)):
        if (i == idx):
            my_list[i] = element
            return my_list
    return my_list
