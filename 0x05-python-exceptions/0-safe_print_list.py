#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        a = 0
        for i in range(0, x):
            print(my_list[i], end="")
            a += 1
        print()
        return a
    except IndexError:
        print()
        return a
