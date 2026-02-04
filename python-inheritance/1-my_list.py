#!/usr/bin/python3
"""Defines a custom list class with a method to print a sorted view.

This module defines MyList, a subclass of list, that can print its elements
in ascending order without modifying the original list.
"""


class MyList(list):
    """Subclass of list with a method to print elements sorted ascending."""
    def print_sorted(self):
        """Print the list in ascending order without modifying the instance.

        Assumes all elements are integers.
        """
        print(sorted(self))
