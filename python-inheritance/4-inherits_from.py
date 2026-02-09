#!/usr/bin/python3
"""4-inherits_from
Defines a function to check whether an object inherits from a specified class.
"""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass
    of a_class; otherwise False.

    The result is False when obj is exactly an instance of a_class.

    Args:
        obj: Any Python object to test.
        a_class: The class to compare against.

    Returns:
        bool: True if type(obj) is a subclass of a_class; otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
