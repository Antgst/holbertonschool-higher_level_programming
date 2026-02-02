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
    """
    Abstract base class that defines the interface for geometric shapes.

    Any subclass must implement:
    - area(): return the shape's area
    - perimeter(): return the shape's perimeter
    """
    @abstractmethod
    def area(self):
        """
        Compute and return the area of the shape.

        Returns:
            float|int: The area of the shape.
        """
        """Return the area of the shape."""
    pass

    @abstractmethod
    def perimeter(self):
        """
        Compute and return the perimeter of the shape.

        Returns:
            float|int: The perimeter of the shape.
        """
    pass


class Circle(Shape):
    """
    Represents a circle defined by a radius.

    Attributes:
        radius (float|int): The radius of the circle.
    """
    def __init__(self, radius=0):
        """
        Initialize a Circle instance.

        Args:
            radius (float|int): The circle radius (default: 0).
        """
        self.radius = radius

    def area(self):
        """
        Compute and return the area of the circle.

        Returns:
            float: The circle area.
        """
        return pi * (self.radius ** 2)

    def perimeter(self):
        """
        Compute and return the perimeter (circumference) of the circle.

        Returns:
            float: The circle perimeter.
        """
        return 2 * pi * self.radius


class Rectangle(Shape):
    """
    Represents a rectangle defined by width and height.

    Attributes:
        width (float|int): The rectangle width.
        height (float|int): The rectangle height.
    """
    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangle instance.

        Args:
            width (float|int): The rectangle width (default: 0).
            height (float|int): The rectangle height (default: 0).
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute and return the area of the rectangle.

        Returns:
            float|int: The rectangle area.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute and return the perimeter of the rectangle.

        Returns:
            float|int: The rectangle perimeter.
        """
        return (self.height * 2) + (self.width * 2)


def shape_info(shape):
    """
    Print the area and perimeter of a shape-like object using duck typing.

    The function does not check the object's type. It assumes the object
    provides area() and perimeter() methods.

    Args:
        shape: Any object implementing area() and perimeter().

    Returns:
        None
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
