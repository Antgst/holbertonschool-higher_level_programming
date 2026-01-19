#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copyoflist = my_list[0:]
    if idx < 0 or idx >= len(my_list):
        return copyoflist
    copyoflist[idx] = element
    return copyoflist
