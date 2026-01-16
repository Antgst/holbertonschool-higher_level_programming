#!/usr/bin/python3

import sys

if __name__ == "__main__":
    add = sum(int(args) 
        for args in sys.argv[1:])
    print(add)
