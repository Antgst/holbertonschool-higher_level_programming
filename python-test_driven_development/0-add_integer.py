#!/usr/bin/python3
"""This module provides a function that adds two numbers
(integers or floats) and returns an integer."""


def add_integer(a, b=98):
    """Add two numbers and return their integer sum.
    Floats are cast to integers before addition.
    Raises TypeError if a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
