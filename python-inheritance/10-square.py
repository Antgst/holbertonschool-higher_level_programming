#!/usr/bin/python3
"""10-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square (a rectangle with equal sides)."""

    def __init__(self, size):
        """Initialize a Square with a validated size.

        Args:
            size (int): Side length (positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return super().area()
