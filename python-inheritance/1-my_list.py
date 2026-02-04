#!/usr/bin/python3
"""Defines MyList, a list subclass with a sorted display helper.

This module provides MyList, which extends the built-in list type and adds
a method to print the elements in ascending order without changing the object.
"""


class MyList(list):
    """List subclass that can print its elements sorted in ascending order."""
    def print_sorted(self):
        """Print the elements in ascending order without modifying the list."""
        print(sorted(self))
