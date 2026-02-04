#!/usr/bin/env python 3
"""
Defines simple animal classes (Fish, Bird) and a multiple-inheritance example
(FlyingFish) that overrides shared behaviors.
"""


class Fish:
    """Represents a fish with basic behaviors and habitat."""
    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message describing the fish's natural habitat (water)."""
        print("The fish lives in water")


class Bird:
    """Represents a bird with basic behaviors and habitat."""
    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message describing the bird's natural habitat (sky)."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represents a flying fish using multiple inheritance (Fish, Bird).

    Overrides swim(), fly(), and habitat() to reflect that
    it can both swim and fly.
    Demonstrates method overriding and how shared
    method names (habitat) are handled.
    """
    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimmming!")

    def fly(self):
        """Print a message indicating that the flying fish is flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print a message describing the flying fish's dual
        habitat (water and sky)."""
        print("The flying fish lives both in water and the sky!")
