#!/usr/bin/python3
"""9-rectangle
Defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle defined by a validated width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height.

        Args:
            width (int): Rectangle width (positive integer).
            height (int): Rectangle height (positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation: [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
