#!/usr/bin/python3
'''Module that provides a function to write text to a UTF-8 file.'''


def write_file(filename="", text=""):
    '''Write a string to a UTF-8 text file and return
    the number of characters written.

    The file is created if it doesn't exist, and
    truncated if it already exists.

    Args:
        filename (str): Path to the file.
        text (str): Text to write to the file.

    Returns:
        int: Number of characters written.'''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
