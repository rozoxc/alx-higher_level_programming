#!/usr/bin/python3
def common_elements(set_1, set_2):
    for element in set_1:
        common_set = set()
        if element in set_2:
            common_set.add(element)
    return common_set
