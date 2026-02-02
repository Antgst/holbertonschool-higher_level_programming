#!/usr/bin/python3
"""11-square
Defines a Square class that inherits from Rectangle.
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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation: [Rectangle] <width>/<height>."""
        return "[rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Represents a square (a rectangle with equal sides)."""
    def __init__(self, size):
        """Initialize a Square with validated size.

        Args:
            size (int): Square size (must be a positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"""
        return self.__size * self.__size

    def __str__(self):
        """"""
        return "[Square] {}/{}".format(self.__size, self.__size)
