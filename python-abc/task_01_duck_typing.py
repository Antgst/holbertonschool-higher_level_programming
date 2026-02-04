#!/usr/bin/env python3
"""
task_01_duck_typing.py

Defines an abstract base class (Shape) and two concrete implementations
(Circle and Rectangle). Also provides a helper function (shape_info) that
uses duck typing to display area and perimeter for any object exposing
area() and perimeter() methods.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Abstract base class that defines the interface for geometric shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Represents a circle defined by a radius."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Compute and return the area of the circle."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Compute and return the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Represents a rectangle defined by width and height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Compute and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Compute and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a
    shape-like object using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
