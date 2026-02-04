#!/usr/bin/env python3
"""
Defines CountedIterator, an iterator wrapper that counts how many items
have been yielded so far.
"""


class CountedIterator:
    """Iterator wrapper that counts the number of values produced."""

    def __init__(self, iterable):
        """Initialize with an iterable and reset the counter to zero."""
        self._iterator = iter(iterable)
        self._count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item and increment the internal counter."""
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        """Return the number of items yielded so far."""
        return self._count
