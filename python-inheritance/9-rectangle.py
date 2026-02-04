#!/usr/bin/python3
"""This module defines Rectangle, a class that extends BaseGeometry with area and string output."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle stores validated width and
    height as private attributes for geometry computations."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance after
        validating width and height as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute and return the rectangle area
        using the stored width and height."""
        return self.__width * self.__height

    def __str__(self):
        """Return the canonical description string
        in the format: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
