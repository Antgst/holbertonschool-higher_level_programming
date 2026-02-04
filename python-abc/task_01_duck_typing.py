#!/usr/bin/env python3
"""
Defines an abstract Shape interface and concrete Circle and Rectangle classes.
Also defines shape_info, a helper that relies on duck typing to display area
and perimeter for any object providing area() and perimeter().
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
    """Circle defined by a radius."""

    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Return the circle area."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Return the circle perimeter."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle defined by a width and a height."""

    def __init__(self, width, height):
        """Initialize a Rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Return the rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter using duck typing, without any type checks."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
