#!/usr/bin/python3
"""Script"""
import sys
save_to_json_file =__import__('5-save_to_json_file').save_to_json_file
load_from_json_file =__import__('6-load_from_json_file').load_from_json_file

name = "add_item.json"
load = []

try:
    load = load_from_json_file(name)
except:
    pass

for i in range(1, len(sys.argv)):
    load.append(sys.argv[i])
save_to_json_file(load, name)
