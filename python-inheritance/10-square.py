#!/usr/bin/python3
"""Defines Square, a class extending Rectangle with a validated size and area computation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square is a Rectangle with equal width and height."""

    def __init__(self, size):
        """Create a Square after validating size as a positive integer."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the square area computed from its size."""
        return self.__size * self.__size
