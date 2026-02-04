#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area()
and an integer validator."""


class BaseGeometry:
    """Geometry base class providing validation helpers."""
    def area(self):
        """Raise an exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a strictly positive integer."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
