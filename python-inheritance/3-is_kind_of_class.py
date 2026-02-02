#!/usr/bin/python3
'''
Defines a function to check if an object is an instance
of a class or its subclasses.

This module provides `is_kind_of_class`, which returns
True when the given object
is an instance of the specified class *or* any subclass of that class.
'''


def is_kind_of_class(obj, a_class):
    '''
    Return True if `obj` is an instance of `a_class` or a subclass; else False.

    Args:
        obj: Any Python object to test.
        a_class: The class to check against.

    Returns:
        bool: True if `obj` is an instance of `a_class` (including subclasses),
        otherwise False.
    '''
    return obj.__class__ == a_class
