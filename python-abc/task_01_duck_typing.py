#!/usr/bin/env python3
"""
This module defines an abstract Shape interface and two concrete classes,
Circle and Rectangle. It also defines shape_info, a helper that relies on
duck typing by calling area() and perimeter() without any explicit type checks.
"""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    """Shape defines the common interface that all
    geometric shapes must provide."""

    @abstractmethod
    def area(self):
        """Compute and return the area value for the current shape instance."""
        raise NotImplementedError

    @abstractmethod
    def perimeter(self):
        """Compute and return the perimeter value
        for the current shape instance."""
        raise NotImplementedError


class Circle(Shape):
    """Circle represents a shape defined by a radius
    and supports area and perimeter."""

    def __init__(self, radius=0):
        """Initialize a Circle instance with a numeric radius value."""
        self.radius = radius

    def area(self):
        """Compute and return the area of the circle using pi * r^2."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Compute and return the circumference of
        the circle using 2 * pi * r."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Rectangle represents a shape defined by width
    and height with area and perimeter."""

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with numeric
        width and height values."""
        self.width = width
        self.height = height

    def area(self):
        """Compute and return the rectangle area using width * height."""
        return self.width * self.height

    def perimeter(self):
        """Compute and return the rectangle perimeter
        using 2 * (width + height)."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter by calling
    area() and perimeter() on the given object."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
