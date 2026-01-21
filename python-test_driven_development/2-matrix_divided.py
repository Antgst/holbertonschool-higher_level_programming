#!/usr/bin/python3
"""This module provides a function that divides all elements
of a matrix by a given number."""


def matrix_divided(matrix, div):
    """Return a new matrix with all elements
    divided by div and rounded to 2 decimals.
    Raises TypeError for invalid matrix or div types,
    and ZeroDivisionError if div is zero.
    """

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
