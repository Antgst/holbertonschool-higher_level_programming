#!/usr/bin/python3
'''Script that adds command-line arguments to a list and saves it as JSON.

The script loads a list from 'add_item.json' if it exists, appends all
command-line arguments to this list, then saves the updated list back to the
same file in JSON format.'''

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

items.extend(sys.argv[1:])
save_to_json_file(items, filename)
