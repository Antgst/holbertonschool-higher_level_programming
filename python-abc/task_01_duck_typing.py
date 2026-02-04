#!/usr/bin/env python3
"""Module demonstrating abstract classes and duck typing with shapes."""

from abc import ABC, abstractmethod
import math


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
        """Initialize a Circle with a non-negative radius."""
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        if radius < 0:
            raise ValueError("radius must be >= 0")
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with non-negative dimensions."""
        if not isinstance(width, (int, float)):
            raise TypeError("width must be a number")
        if not isinstance(height, (int, float)):
            raise TypeError("height must be a number")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape using duck typing."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
