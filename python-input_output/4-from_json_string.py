#!/usr/bin/python3
'''Module that provides a function to convert a JSON
string into a Python object.'''

import json


def from_json_string(my_str):
    '''
    Return the Python object represented by a JSON string.

    Args:
        my_str (str): JSON-formatted string.

    Returns:
        object: The Python data structure represented by the JSON string.'''
    return json.loads(my_str)
