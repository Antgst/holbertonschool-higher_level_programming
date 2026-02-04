#!/usr/bin/env python3
"""
Defines SwimMixin and FlyMixin, and a Dragon class that combines both behaviors.
"""


class SwimMixin:
    """Mixin that provides swimming behavior."""

    def swim(self):
        """Print a message indicating that the creature swims."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying behavior."""

    def fly(self):
        """Print a message indicating that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can swim and fly by combining mixins."""

    def roar(self):
        """Print a message indicating that the dragon roars."""
        print("The dragon roars!")
