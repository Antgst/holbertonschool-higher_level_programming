#!/usr/bin/python3
"""7-base_geometry
Defines a BaseGeometry class with area() and integer_validator().
"""


class BaseGeometry:
    """Base class for geometry objects."""
    def area(self):
        """Raise an Exception because area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
