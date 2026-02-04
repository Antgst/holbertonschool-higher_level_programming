#!/usr/bin/env python3
"""
Defines Fish and Bird parent classes, plus FlyingFish using multiple inheritance.
"""


class Fish:
    """Fish with swim behavior and a water habitat."""

    def swim(self):
        """Print a message indicating that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print a message describing the fish habitat."""
        print("The fish lives in water")


class Bird:
    """Bird with fly behavior and a sky habitat."""

    def fly(self):
        """Print a message indicating that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print a message describing the bird habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish inherits from Fish and Bird and overrides key behaviors."""

    def swim(self):
        """Print a message indicating that the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Print a message indicating that the flying fish is soaring."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Print a message describing the flying fish dual habitat."""
        print("The flying fish lives both in water and the sky!")
