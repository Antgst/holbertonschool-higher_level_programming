#!/usr/bin/python3
"""Defines Rectangle, a class extending BaseGeometry with area computation and formatted output."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle keeps validated width and height as private attributes."""

    def __init__(self, width, height):
        """Create a Rectangle after validating
        width and height as positive integers."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area computed from the stored width and height."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description string formatted
        as: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
