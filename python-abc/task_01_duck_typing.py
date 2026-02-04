#!/usr/bin/env python3
"""
Defines an abstract Shape interface and concrete Circle and Rectangle classes.
Includes shape_info(), which relies on duck typing (no explicit type checks).
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle defined by a radius."""

    def __init__(self, radius):
        """Initialize a Circle with a radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape (duck typing)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
