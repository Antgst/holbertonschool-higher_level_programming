#!/usr/bin/python3
"""6-base_geometry
Defines a BaseGeometry class with an unimplemented area() method.
"""


class BaseGeometry:
    """Base class for geometry objects."""
    def area(self):
        """Raise an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")
