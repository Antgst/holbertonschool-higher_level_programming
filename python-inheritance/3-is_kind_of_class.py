#!/usr/bin/python3
'''
3-is_kind_of_class
Defines a function to check whether an object is an instance of a class
or of a class that inherits from it.
'''


def is_kind_of_class(obj, a_class):
    '''
    Return True if obj is an instance of a_class; otherwise False.

    This includes instances of subclasses of a_class.

    Args:
        obj: Any Python object to test.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class (directly or indirectly);
        otherwise False.
    '''
    return isinstance(obj, a_class)
