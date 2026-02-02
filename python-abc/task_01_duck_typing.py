#!/usr/bin/env python3
"""
task_01_duck_typing.py
"""


from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Return the area of the shape."""
    pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
    pass


class Circle(Shape):
    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.height * 2) + (self.width * 2)


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
