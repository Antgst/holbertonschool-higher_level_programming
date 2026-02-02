#!/usr/bin/python3
'''
Defines a function that checks if an object is exactly an instance of a class.

This module provides `is_same_class`, which returns True only when the object's
type is exactly the specified class (not a subclass).
'''


def is_same_class(obj, a_class):
    '''Return True if `obj` is exactly an instance of `a_class`, else False.

    Args:
        obj: Any Python object to test.
        a_class: The class to compare against.

    Returns:
        bool: True if type(obj) is exactly a_class, otherwise False.'''
    return obj.__class__ == a_class
