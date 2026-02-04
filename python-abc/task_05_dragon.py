#!/usr/bin/env python 3
"""
Defines mixins for swimming and flying behaviors, and a Dragon class that
combines them via multiple inheritance.
"""


class SwimMixin:
    """Mixin that adds a swimming behavior to a class."""
    def swing(self):
        """Print a message indicating that the creature swims.

        Note:
            The method name is `swing` in the provided code. If the intended
            behavior is "swim", consider renaming it to `swim` for clarity.
        """
        print("The creature swims")


class FlyMixin:
    """Mixin that adds a flying behavior to a class."""
    def fly(self):
        """Print a message indicating that the creature flies."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon that can both swim and fly thanks to mixins.

    Inherits:
        SwimMixin: Provides swimming behavior.
        FlyMixin: Provides flying behavior.
    """
    def roar(self):
        """Print a message indicating that the dragon roars."""
        print("The dragon roars!")
