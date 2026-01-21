#!/usr/bin/python3
"""This module provides a function that prints
a text with indentation rules."""


def text_indentation(text):
    """Print text with two new lines after '.', '?' and ':'.

    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for ch in text:
        line += ch
        if ch in ".?:":
            print(line.strip())
            print()
            line = ""

    if line.strip():
        print(line.strip(), end="")
