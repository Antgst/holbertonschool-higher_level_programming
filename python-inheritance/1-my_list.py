#!/usr/bin/python 3
"""Defines a custom list class with a method to print a sorted view.

This module provides the MyList class, which inherits from Python's built-in
list and adds a method to print the list elements in ascending order without
modifying the original list."""


class MyList(list):
    """
    Custom list that can print its elements sorted in ascending order.
    """
    def print_sorted(self):
        """
        Print the list sorted in ascending order without modifying itself.
        """
        print(sorted(self))
