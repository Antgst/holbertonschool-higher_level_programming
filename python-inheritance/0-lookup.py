#!/usr/bin/python3
'''Defines a utility function to list an object's
available attributes and methods.

This module provides the `lookup` function,
which returns a list of attribute and
method names accessible on a given object.
'''


def lookup(obj):
    '''Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object to introspect.

    Returns:
        list: A list of strings containing attribute and method names.

    Example:
        >>> lookup([1, 2, 3])  # doctest: +ELLIPSIS
        ['__add__', ..., 'append', ...]
        '''
    return dir(obj)
