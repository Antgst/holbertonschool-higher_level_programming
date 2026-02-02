#!/usr/bin/python3
"""8-rectangle
Defines BaseGeometry and a Rectangle class that inherits from it.
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
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")


class Rectangle(BaseGeometry):
    """Represents a rectangle defined by its width and height."""
    def __init__(self, width, height):
        """Initialize a Rectangle with validated width and height.

        Args:
            width (int): Rectangle width (must be a positive integer).
            height (int): Rectangle height (must be a positive integer).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
