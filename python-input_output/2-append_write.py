#!/usr/bin/python3
'''Module that provides a function to append text to a UTF-8 file.'''


def append_write(filename="", text=""):
    '''Append a string to a UTF-8 text file and return
    the number of characters added.

    Args:
        filename (str): Path to the file.
        text (str): Text to append to the file.

    Returns:
        int: Number of characters written.'''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
