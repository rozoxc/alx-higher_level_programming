#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sum = 0
    num_arg = len(sys.argv) - 1
    if num_arg == 0:
        print("0")
    else:
        for i in range(1, num_arg + 1):
            sum += int(sys.argv[i])
        print(sum)
