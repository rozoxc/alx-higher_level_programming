#!/usr/bin/python3
def pow(a, b):
    r = 1
    if b >= 0:
        for _ in range(b):
            r *= a
    else:
        for _ in range(-b):
            r /= a
    return r
