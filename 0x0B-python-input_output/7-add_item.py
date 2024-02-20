#!/usr/bin/python3
"""Adds all arguments to a Python list and saves them to a file."""
import sys
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        json_list = load_from_json_file('add_item.json')
    except FileNotFoundError:
        json_list = []

    json_list.extend(sys.argv[1:])
    save_to_json_file(json_list, "add_item.json")
