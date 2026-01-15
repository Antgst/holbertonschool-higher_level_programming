#!/usr/bin/python3

import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1"" argument:".format(sys.argv[1]))
        print("1"" ""{}".format(sys.argv[1]))
    else:
        print("{}"": ""{}".format(argc, sys.argv[1:]))
        for i, args in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(i, args))
