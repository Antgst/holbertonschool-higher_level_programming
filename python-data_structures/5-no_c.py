#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return ""
    newstring = ""
    for ch in my_string:
        if ch != 'C' and ch != 'c':
            newstring += ch
    return newstring
