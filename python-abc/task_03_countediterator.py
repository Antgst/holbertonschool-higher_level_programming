#!/usr/bin/env python 3
"""
Defines CountedIterator, an iterator wrapper that counts how many items
have been yielded so far.
"""


class CountedIterator:
    """Iterator wrapper that counts the number of values produced.

    This class wraps any iterable, exposes the standard iterator protocol
    (__iter__ and __next__), and increments an internal counter each time
    an element is returned by __next__.

    Attributes:
        iterator (iterator): The underlying iterator built from the iterable.
        count (int): Number of items that have been yielded so far.
    """

    def __init__(self, iterable):
        """Initialize a CountedIterator from an iterable.

        Args:
            iterable: Any object that can be iterated
            over (implements __iter__).

        Side Effects:
            Creates an iterator from `iterable`
            and initializes the counter to 0.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself.

        Returns:
            CountedIterator: Self, to support iteration (e.g., in a for-loop).
        """
        return self

    def __next__(self):
        """Return the next item from the underlying
        iterator and increment count.

        Returns:
            Any: The next element produced by the wrapped iterator.

        Raises:
            StopIteration: When the underlying iterator is exhausted.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def counter(self):
        """Return how many items have been yielded so far.

        Returns:
            int: The current number of yielded items.
        """
        return self.count
