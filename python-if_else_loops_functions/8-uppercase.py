#!/usr/bin/python3
def uppercase(str):
    final = ""
    for i in str:
        if 'a' <= i <= 'z':
            final += chr(ord(i) - 32)
        else:
            final += i
    print("{}".format(final))
