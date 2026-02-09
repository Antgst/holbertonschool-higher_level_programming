#!/usr/bin/python3
'''
2-is_same_class
Defines a function to check whether an object
is exactly an instance of a class.
'''


def is_same_class(obj, a_class):
    '''Return True if obj is exactly an instance of a_class; otherwise False.

    Args:
        obj: Any Python object to test.
        a_class: The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class; otherwise False.'''
    return type(obj) is a_class
