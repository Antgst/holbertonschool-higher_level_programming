#!/usr/bin/python3
"""This module defines BaseGeometry with an
unimplemented area method and an integer validator."""


class BaseGeometry:
    """BaseGeometry provides basic validation helpers for geometry classes."""

    def area(self):
        """Raise an exception to indicate that
        area computation is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly
        positive integer for the given attribute name."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
